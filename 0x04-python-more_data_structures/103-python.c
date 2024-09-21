#include <Python.h>
#include <object.h>
#include <listobject.h>
#include <bytesobject.h>
#include <stdio.h>
#include "lists.h"

void print_python_list(PyObject *p)
{
    if (!PyList_Check(p)) {
        printf("[ERROR] Invalid List Object\n");
        return;
    }

    Py_ssize_t size = PyList_Size(p);
    Py_ssize_t allocated = ((PyListObject *)p)->allocated;

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %zd\n", size);
    printf("[*] Allocated = %zd\n", allocated);

    for (Py_ssize_t i = 0; i < size; i++) {
        PyObject *item = PyList_GetItem(p, i);
        const char *type_name = item->ob_type->tp_name;
        printf("Element %zd: %s\n", i, type_name);

        // If the element is a bytes object, print its info
        if (PyBytes_Check(item)) {
            print_python_bytes(item);
        }
    }
}

void print_python_bytes(PyObject *p)
{
    if (!PyBytes_Check(p)) {
        printf("[.] bytes object info\n");
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    Py_ssize_t size = PyBytes_Size(p);
    char *bytes_string = PyBytes_AsString(p);

    printf("[.] bytes object info\n");
    printf("  size: %zd\n", size);
    printf("  trying string: %s\n", bytes_string);

    printf("  first %zd bytes: ", size < 10 ? size + 1 : 10);
    for (Py_ssize_t i = 0; i < size && i < 10; i++) {
        printf("%02x", (unsigned char)bytes_string[i]);
        if (i < size - 1 && i <
