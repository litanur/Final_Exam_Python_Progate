import random
import datetime
from customer import Customer

class ATMProgram:
    atm = Customer(id)

    while True:
        id = int(input('Masukkan pin Anda: '))
        trial = 1

        while (id != int(atm.cekPin())):
            id = int(input('Pin Anda salah. Silakan masukkan lagi: '))
            trial += 1

            if trial == 3:
                print('Error. Silakan ambil kartu dan coba lagi..')
                exit()

        while True:
            print('\n==============================')
            print('Selamat datang  di ATM Progate..')
            print('\n1. Cek saldo \n2. Debet \n3. Deposit \n4. Ganti pin\n5. Keluar')

            selected_menu = int(input('Silakan pilih menu: '))

            if selected_menu == 1:
                print('Saldo Anda sekarang: Rp ' + str(atm.cekSaldo()) + '\n')

            elif selected_menu == 2:
                amount = float(input('Masukkan nominal saldo: '))
                verify_withdraw = input('Konfirmasi: Anda akan mendebet saldo dengan nominal ' + str(amount) + ' ? y/n\n')

                if verify_withdraw == 'y':
                    print('Saldo awal Anda adalah Rp ' + str(atm.cekSaldo()))
                else:
                    break

                if amount < atm.cekSaldo():
                    atm.withDrawBalance(amount)
                    print('Transaksi debet berhasil!')
                    print('Sisa saldo: Rp ' + str(atm.cekSaldo()))
                else:
                    print('Maaf. Saldo Anda tidak cukup untuk melakukan debet!')
                    print('Silakan deposit terlebih dahulu')

            elif selected_menu == 3:
                amount = float(input('Masukkan nominal saldo: '))
                verify_deposit = input('Konfirmasi: Anda akan deposit dengan nominal ' + str(amount) + ' ? y/n\n')

                if verify_deposit == 'y':
                    atm.depositBalance(amount)
                    print('Saldo Anda sekarang adalah Rp ' + str(atm.cekSaldo()))
                else:
                    break

            elif selected_menu == 4:
                verify_pin = int(input('Masukkan pin Anda: '))

                while verify_pin != int(atm.cekPin()):
                    print('Pin Anda salah. Silakan masukkan pin kembali.')

                updated_pin = int(input('Silakan masukkan pin baru: '))
                verify_newpin = int(input('Masukkan pin baru lagi: '))

                if verify_pin == updated_pin:
                    print('Pin berhasil diganti!')
                else:
                    print('Maaf. Konfirmasi pin baru tidak berhasil. Pin Anda tidak berhasil diganti!')
            elif selected_menu == 5:
                print('Resi tercetak otomatis saat Anda keluar. \nHarap simpan tanda terima ini \nsebagai bukti transaksi Anda')
                print('No. record: ' + str(random.randint(10000, 1000000)))
                print('Tanggal: ' + str(datetime.datetime.now()))
                print('Saldo akhir: ' + str(atm.cekSaldo()))
                print('Terima kasih telah menggunakan ATM Progate')
                exit()
            else:
                print('Error. Menu tidak tersedia')
