#include <Python.h>

void print_python_list(PyObject *p)
{
    Py_ssize_t size, alloc, i;
    PyObject *item;

    printf("[*] Python list info\n");
    if (!PyList_Check(p))
    {
        printf("  [ERROR] Invalid List Object\n");
        return;
    }

    size = ((PyVarObject *)p)->ob_size;
    alloc = ((PyListObject *)p)->allocated;

    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", alloc);

    for (i = 0; i < size; i++)
    {
        item = ((PyListObject *)p)->ob_item[i];
        printf("Element %ld: %s\n", i, item->ob_type->tp_name);
        if (PyBytes_Check(item))
            print_python_bytes(item);
    }
}

void print_python_bytes(PyObject *p)
{
    Py_ssize_t size, i;
    char *str;

    printf("[.] bytes object info\n");
    if (!PyBytes_Check(p))
    {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    size = ((PyVarObject *)p)->ob_size;
    str = ((PyBytesObject *)p)->ob_sval;

    printf("  size: %ld\n", size);
    printf("  trying string: %s\n", str);

    printf("  first %ld bytes:", size < 10 ? size + 1 : 10);
    for (i = 0; i < size && i < 10; i++)
        printf(" %02x", (unsigned char)str[i]);
    printf("\n");
}
