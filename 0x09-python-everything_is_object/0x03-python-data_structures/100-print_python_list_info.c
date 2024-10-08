#include <Python.h>

/**
 * print_python_list_info - Prints basic information about a Python list.
 * @p: Pointer to the Python object.
 */
void print_python_list_info(PyObject *p)
{
    // Ensure that the object is a Python list
    if (!PyList_Check(p))
    {
        PyErr_Print();
        return;
    }

    // Get the size of the list
    Py_ssize_t size = PyList_Size(p);
    printf("[*] Size of the Python List = %zd\n", size);

    // Print type of each element in the list
    printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);
    for (Py_ssize_t i = 0; i < size; i++)
    {
        PyObject *item = PyList_GetItem(p, i);
        printf("Element %zd: %s\n", i, Py_TYPE(item)->tp_name);
    }
}
