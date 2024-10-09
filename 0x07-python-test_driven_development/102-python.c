#include <Python.h>
#include <stdio.h>
#include <stdlib.h>
#include <wchar.h>
#include <locale.h>

/**
 * print_python_string - Print Python string information
 * @p: Python string object
 */
void print_python_string(PyObject *p)
{
    wchar_t *str;
    Py_ssize_t len;
    PyObject *str_repr;

    setlocale(LC_ALL, "");
    printf("[.] string object info\n");

    if (!PyUnicode_Check(p))
    {
        printf("  [ERROR] Invalid String Object\n");
        return;
    }

    if (PyUnicode_IS_COMPACT_ASCII(p))
        printf("  type: compact ascii\n");
    else
        printf("  type: compact unicode object\n");

    len = PyUnicode_GET_LENGTH(p);
    str = PyUnicode_AsWideCharString(p, &len);

    printf("  length: %ld\n", len);
    printf("  value: %ls\n", str);

    PyMem_Free(str);
}
