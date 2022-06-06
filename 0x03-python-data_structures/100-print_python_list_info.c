#include <stdio.h>
#include <stdlib.h>
#include <Python.h>
/**
  * print_python_list_info - Print python list info
  * @p: modulo object
  * Return: Nothing
  */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t i, size = (((PyVarObject *)(p))->ob_size);
	Py_ssize_t allo = (((PyListObject *)(p))->allocated);
	PyObject *ele;

	printf("[*] Size of the Python List = %zd\n", size);
	printf("[*] Allocated = %zd\n", allo);

	for (i = 0; i < size; i++)
	{
		ele = PyList_GetItem(p, i);
		printf("Element %zd: %s\n", i, (char *)(ele->ob_type)->tp_name);
	}
}
