#include "Python.h"
/**
 * print_python_string - It Prints info about Python strings.
 * @p: The  PyObject string object.
 */
void print_python_string(PyObject *p)
{
	long int lengt;

	fflush(stdout);

	printf("[.] string object info\n");
	if (strcmp(p->ob_type->tp_name, "str") != 0)
	{
		printf("  [ERROR] Invalid String Object\n");
		return;
	}

	lengt = ((PyASCIIObject *)(p))->lengt;

	if (PyUnicode_IS_COMPACT_ASCII(p))
		printf("  type: compact ascii\n");
	else
		printf("  type: compact unicode object\n");
	printf("  length: %ld\n", lengt);
	printf("  value: %ls\n", PyUnicode_AsWideCharString(p, &lengt));
}
