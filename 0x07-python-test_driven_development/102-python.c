#include <stdio.h>
#include <sys/types.h>
#include <pyport.h>
#include <assert.h>
#include <object.h>
#include <unicodeobject.h>
#include <tupleobject.h>
#include <structseq.h>
#include <listobject.h>
#include <bytesobject.h>
#include <floatobject.h>
#include <pystrtod.h>
#include <string.h>

/**
 * print_python_string - yes
 * @p: Python object
 */
void print_python_string(PyObject *p)
{
	PyObject *str_value;
	char *str_type;
	int i = 0, max;

	setbuf(stdout, NULL);
	printf("[.] string object info\n");

	if (!PyUnicode_Check(p))
	{
		fprintf(stdout, "  [ERROR] Invalid Bytes Object\n");
		return;
	}

	str_type = PyUnicode_IS_COMPACT_ASCII(p) ? "ascii" : "unicode object";
	printf("  type: compact %s\n", str_type);

	printf("  length: %ld\n", PyUnicode_GET_LENGTH(p));

	str_value = PyUnicode_AsEncodedString(p, "utf-8", "~E~");
	printf("  value: %s\n", PyBytes_AsString(str_value));
}
