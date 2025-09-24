# Runs code and test cases automatically

# MVP: Automatic Code Tester
import sys
import io

def run_code_and_test(code_str, test_func, *args, **kwargs):
    # Redirect stdout to capture print statements
    old_stdout = sys.stdout
    sys.stdout = mystdout = io.StringIO()
    try:
        exec(code_str, globals())
        result = test_func(*args, **kwargs)
        output = mystdout.getvalue()
        return True, result, output
    except Exception as e:
        return False, None, str(e)
    finally:
        sys.stdout = old_stdout

# Example usage
if __name__ == "__main__":
    code = "def add(a, b):\n    return a + b"
    # Define test function as a string to exec in the same namespace
    test_code = "def test():\n    return add(2, 3) == 5"
    namespace = {}
    exec(code, namespace)
    exec(test_code, namespace)
    passed, result, output = run_code_and_test(code + "\n" + test_code, namespace['test'])
    print(f"Test passed: {passed}, Output: {output}")

