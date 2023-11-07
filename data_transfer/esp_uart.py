import serial


class serial_reader:
    def __init__(self) -> None:
        com_port = '/dev/tty' # TO_DO
        baud_rate = 115200
        self.ser = serial.Serial(com_port, baud_rate)
        
    def esp_reader(self, audio_code = 0, magnet_mode = 0, led_mode = 0):

        '''
        получаем актуальные управляюще команды!! (audio_code magnet_mode led_mode )
        '''
        flame, magnet_status, sonic_dist= -1, -1, -1

        data_to_send = '#' + audio_code + ',' + magnet_mode + ',' + led_mode + ';'
        self.ser.write(data_to_send.encode())
        received_data = self.ser.readline().decode()
        

        if received_data[0] == "%" and received_data[-1] == ";":
            try:
                flame, magnet_status, sonic_dist = \
                    map(int, received_data[1:-1].split(','))
            except:
                flame, magnet_status, sonic_dist= -1, -1, -1

        # print([flame, magnet_status, sonic_dist])
        return bool(flame), bool(magnet_status), sonic_dist

    def ser_close(self): 
        self.ser.close()

