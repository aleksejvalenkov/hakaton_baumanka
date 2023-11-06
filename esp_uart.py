import serial

com_port = '/dev/tty' # TO_DO
baud_rate = 115200

is_sending = True

audio_code = 0
magnet_mode = 0
led_mode = 0

flame = None
magnet_status = None
sonic_dist = None


while is_sending:

    '''
    получаем актуальные управляюще команды!! (audio_code magnet_mode led_mode )
    '''

    ser = serial.Serial(com_port, baud_rate)

    data_to_send = '#' + audio_code + ',' + magnet_mode + ',' + led_mode + ';'
    ser.write(data_to_send.encode())
    received_data = ser.readline().decode()
    ser.close()

    if received_data[0] == "%" and received_data[-1] == ";":
        try:
            flame, magnet_status, sonic_dist = \
                map(int, received_data[1:-1].split(','))
        except:
            flame, magnet_status, sonic_dist= -1, -1, -1

    print([flame, magnet_status, sonic_dist])

    '''
    че-то делаем с данными
    '''



