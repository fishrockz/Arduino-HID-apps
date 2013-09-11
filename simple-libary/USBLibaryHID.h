


#define usblib_ENABLED 1


class willslibUSBLib_ 
{
private:
	//ring_buffer *_cdc_rx_buffer;
	int flag;
	int * VarWatch;
public:
	
	void Func(void);
	void reset(void);
	void setwatch(int* data);
	/*void begin(uint16_t baud_count);
	void end(void);

	virtual int available(void);
	virtual void accept(void);
	virtual int peek(void);
	virtual int read(void);
	virtual void flush(void);
	virtual size_t write(uint8_t);
	using Print::write; // pull in write(str) and write(buf, size) from Print
	operator bool();*/
};
extern willslibUSBLib_ willslibUSBLib;
