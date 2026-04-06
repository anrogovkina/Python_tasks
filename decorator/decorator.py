import functools
import time


def cache_decorator(depth=10, ttl=None):
    def decorator(func):
        cache = {}
        order = []
        hits = 0
        misses = 0

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            nonlocal hits, misses
            kwargs_items = tuple(sorted(kwargs.items()))
            key = (args, kwargs_items)
            current_time = time.time()

            if key in cache:
                value, expire_time = cache[key]
                # Берем значение из кэша, если его время жизни не истекло
                if ttl is None or current_time < expire_time:
                    hits += 1
                    print("Значение взято из кэша.")
                    return value
                else:
                    # Удаляем значение из кэша, если оно устарело
                    print("Значение в кэше устарело.")
                    del cache[key]
                    if key in order:
                        order.remove(key)

            misses += 1
            result = func(*args, **kwargs)
            if ttl is None:
                expire_time = None
            else:
                expire_time = current_time + ttl

            cache[key] = (result, expire_time)
            order.append(key)

            # Удаление значения из кэша при превышении глубины кэша
            if len(cache) > depth:
                old_key = order.pop(0)
                del cache[old_key]
                print("Достигнута максимальная длина кэша. Старое значение удалено.")
            return result

        # Статистика кэша
        def cache_stats():
            return {
                "Попадания:": hits,
                "Промахи:": misses,
                "Глубина кэша:": len(cache),
                "Максимальная глубина:": depth,
                "Время жизни:": ttl
            }

        # Очистка кэша
        def clear_cache():
            nonlocal hits, misses
            cache.clear()
            order.clear()
            hits = 0
            misses = 0
            print("Кэш очищен")

        wrapper.cache_stats = cache_stats
        wrapper.clear_cache = clear_cache
        return wrapper

    return decorator


# Пример использования
if __name__ == "__main__":
    # Для одной функции
    @cache_decorator(3, 1)
    def test_function(x):
        return x ** 2


    print(test_function(3))  # вычисляется
    print(test_function(3))  # из кэша
    print(test_function(4))
    print(test_function(5))
    print(test_function(6))  # удаление старого значения из кэша, так как достигнута максимальная глубина
    print(test_function(7))
    time.sleep(2)
    print(test_function(7))  # истечение времени жизни кэша

    # Статистика кэша для функции test_function
    print("\nСТАТИСТИКА:")
    stats = test_function.cache_stats()
    for key, value in stats.items():
        print(key, value)

    # Очистка кэша
    print("\nОЧИСТКА КЭША")
    test_function.clear_cache()

    print("Статистика после очистки:")
    stats = test_function.cache_stats()
    for key, value in stats.items():
        print(key, value)


    # Для нескольких функций
    @cache_decorator(7)
    def test1(x):
        return x ** 2


    @cache_decorator(5)
    def test2(x):
        return x * 5


    print(test1(3))  # вычисляется
    print(test2(3))  # вычисляется
    print(test1(3))  # из кэша
    print(test2(3))  # из кэша