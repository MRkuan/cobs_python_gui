/*
 * StuffData byte stuffs ¡°length¡± bytes of
 * data at the location pointed to by ¡°ptr¡±,
 * writing the output to the location pointed
 * to by ¡°dst¡±.
 */

#define FinishBlock(X) (*code_ptr = (X), \
						code_ptr = dst++, \
						code = 0x01 )
 void StuffData(const unsigned char *ptr, unsigned long length,
		unsigned char *dst)
{
	const unsigned char *end = ptr + length;
	unsigned char *code_ptr = dst++;
	unsigned char code = 0x01;
	while (ptr < end)
	{
		if (*ptr == 0)
			FinishBlock(code);
		else
		{
			*dst++ = *ptr;
			code++;
			if (code == 0xFF)
				FinishBlock(code);
		}
        ptr++;
	}
	FinishBlock(code);
}

/*
 * UnStuffData decodes ¡°length¡± bytes of
 * data at the location pointed to by ¡°ptr¡±,
 * writing the output to the location pointed
 * to by ¡°dst¡±.
 */
 void UnStuffData(const unsigned char *ptr, unsigned long length,
		unsigned char *dst)
{
	const unsigned char *end = ptr + length;
	while (ptr < end)
	{
		int i, code = *ptr++;
		for (i = 1; i < code; i++)
			*dst++ = *ptr++;
		if (code < 0xFF)
			*dst++ = 0;
	}
}

 int main(void)
 {
     unsigned char data[100] = { 0x02,0x06,0x02,0x5B,0xD8 };
     unsigned long datLen = 5;

     unsigned char  out_data[100] = { 0 };
 
     UnStuffData(data, datLen, out_data);
 
 
 

 
     getchar();
     return 0;
 }