
# import library
import pandas as pd 
import streamlit as st 

# library for visualization
import matplotlib.pyplot as plt 
import seaborn as sns

def run():
    # set title
    st.title('Bank Marketing Campaign Analysis')

    # garis pembatas
    st.write('___')

    # gambar
    st.image('https://blog.pintu.co.id/wp-content/uploads/2023/08/investasi-deposito.jpg')

    # garis pembatas
    st.write('___')

    # sub judul
    st.write('# Dataframe')

    # load data
    df = pd.read_csv('bank.csv')

    # show data
    st.dataframe(df)

    # df. info
    st.write('''
**Usia:**
- Rata-rata usia nasabah adalah 39 tahun dengan rentang umur mulai dari 18 - 95 tahun, dimana kebanyakan nasabah berumur lebih muda dan ada beberapa yang usianya jauh lebih tua. Melihat dari rata-ratanya dan berdasarkan [rata-rata usia menikah bangsa eropa](https://www.statista.com/statistics/612174/mean-age-at-first-marriage-in-european-countries/), kemungkinan besar bahwa rata-rata nasabah sudah menikah, memiliki pekerjaan dan tanggungan rumah.

**Saldo:**
- Rata-rata saldo nasabah adalah 255 EUR dengan rentang saldo yang ada pada data mulai dari -6847 EUR - 81204 EUR. berdasarkan [sebuah website finansial](https://www.sofi.com/learn/content/negative-bank-balance/), adanya saldo minus menunjukan ada beberapa nasabah yang memiliki hutang ke bank, sedangkan standart deviasi yang jauh lebih tinggi dari mean serta skewness yang cukup tinggi menunjuknan adanya beberapa nasabah-nasabah yang berasal dari kaum elit sehingga saldo tertinggi pada data ada di angka 81204 EUR.

**Durasi telepon per nasabah:**
- Durasi waktu telepon rata-rata per nasabah pada kegiatan pemasaran sebelumnya adalah 255 detik atau sekitar 4.5 menit, durasi telepon kebanyakan nasabah lebih cepat dan ada beberapa yang membutuhkan waktu telepon lebih lama dari yang lainnya dengan durasi tercepat 2 detik dan terlama 1 jam. Hal ini mungkin dipengaruhi oleh ketertarikan nasabah pada campaign-nya, dimana nasabah yang tertarik biasanya membutuhkan waktu lebih lama.

**Banyaknya Kontak ketika Kampanye:**
- Rata-rata kontak yang dilakukan selama kampanye adalah 2 kali per nasabah. Kebanyakan nasabah mendapatkan telepon 1-3 kali saja, namun ada beberapa nasabah yang mendapat telepon sampai 63 kali.

**Lama setelah kontak terakhir:**
- Rata-rata lamanya hari setelah kontak terakhir pada kampanye sebelumnya adalah 0. Nilai minimal sampai dengan nilai tengah yang konsisten menunjukkan angka 0 mengindikasikan bahwa dalam kampanye kali ini kebanyakan nasabah merupakan orang-orang yang baru saja diikutkan dalam kampanye dan ada beberapa yang sudah diikutkan dari kampanye sebelumnya.

**Banyaknya Kontak sebelum Kampanye:**
- Rata-rata kontak yang dilakukan sebelum kampanye ini juga 0. Sama dengan lamanya hari setelah kontak terakhir pada kampanye sebelumnya, Nilai minimal sampai dengan nilai tengah juga menunjukkan angka 0 yang mengindikasikan sebagian besar merupakan nasabah yang baru bergabung pada kampanye kali ini.
             ''')

    # edit df
    # inisiasi list untuk menampung week
    week = []

    # loop deteksi minggu berdasarkan tanggal
    for i in df['day']:
        # kondisi tanggal 1-7
        if i <= 7:
            # add minggu ke-1 ke list
            week.append(1)
        # kondisi tanggal 8-14
        elif i <= 14:
            # add minggu ke-2 ke list
            week.append(2)
        # kondisi tanggal 15-21
        elif i <= 21:
            # add minggu ke-3 ke list
            week.append(3)
        # kondisi tanggal 22-31
        elif 21 < i <= 31:
            # add minggu ke-4 ke list
            week.append(4)
        # kondisi lainnya
        else:
            # add NA ke list0
            week.append(pd.NA)

    # add 'week' to dataframe
    df['week'] = week

    # replace -1 dengan 0
    df['pdays'].replace(-1,0,inplace=True)

    # convert week to object
    df['week'] = df['week'].astype(object)

    # convert day to object
    df['day'] = df['day'].astype(object)

    # univariate
    st.write('# Univariate Analysis')

    # perbandingan kolom target
    st.write('## Perbandingan Target')

    # create canvas
    fig = plt.figure(figsize=(15,10))

    # plot
    # value counts
    deposit = df['deposit'].value_counts()

    count = deposit.values
    label = deposit.index

    plt.pie(count, labels=label, 
            autopct='%1.1f%%',
            colors=['lightblue','lightgreen'])
    plt.title('Deposit Rate')
    plt.axis('equal')

    # show plot
    st.pyplot(fig)

    # inisgth
    st.write('''
**Distribusi Target Cukup Seimbang:**\n
Pie chart menunjukkan bahwa kategori "no" sebesar 52.6% dan "yes" sebesar 47.4%. Meskipun ada sedikit ketidakseimbangan dengan kategori "no" yang 5.2% lebih tinggi daripada "yes," distribusi ini cukup seimbang.
             ''')

    # distribusi numerik
    st.write('## Distribusi Numerik')

    # create canvas
    fig = plt.figure(figsize=(15,10))

    # set num cat
    num = ['age', 'balance', 'duration', 'campaign', 'pdays', 'previous']
    cat = df.drop(columns=num).columns.tolist()

    # loop  buat histplot unutk setiap kolom
    for i in range(0,len(num)):
        # set subplot 2x3
        plt.subplot(2, 3, i+1)
        
        # buat histplot
        sns.histplot(df[num[i]], kde=True, bins=20)

        # add gridline
        plt.grid(True, linestyle = '--', color = 'grey', alpha = 0.3)
        # add title
        plt.title(f'Distribution of {num[i]}')

    # show plot
    st.pyplot(fig)

    # insight
    st.write('''
Secara keseluruhan baik pada umur, saldo, durasi telepon, banyaknya kontak yang dilakukan selama kampanye, lamanya hari setelah kampanye terakhir, dan juga banyaknya kontak yang dilakukan sebelum kampanye dimulai menunjukkan bahwa kebanyakan nasabah memiliki nilai yang rendah dan ada beberapa yang nilainya lebih tinggi.

- **Usia Nasabah:** Kebanyakan nasabah berumur antara 30-50 tahun, menunjukkan bahwa mereka berada di usia produktif. Namun, ada juga beberapa nasabah yang jauh lebih tua.

- **Saldo Nasabah:** Mayoritas nasabah memiliki saldo kurang dari 5000 EUR, dengan beberapa nasabah memiliki saldo yang jauh lebih tinggi.

- **Durasi Telepon:** Sebagian besar nasabah membutuhkan waktu yang singkat dalam percakapan telepon, namun ada beberapa yang membutuhkan waktu lebih lama, hingga satu jam.

- **Jumlah Kontak Selama Kampanye:** Rata-rata nasabah dihubungi dua kali selama kampanye. Sebagian besar hanya dihubungi 1-3 kali, meskipun ada yang dihubungi hingga 63 kali.

- **Lamanya Hari Setelah Kontak Terakhir pada Kampanye Sebelumnya:** Rata-rata menunjukkan angka 0, yang berarti mayoritas nasabah baru pertama kali diikutsertakan dalam kampanye ini.

- **Jumlah Kontak Sebelum Kampanye Ini:** Sama dengan lamanya hari setelah kontak terakhir, sebagian besar nasabah baru bergabung pada kampanye kali ini.
''')

    # distribusi kategorik
    st.write('## Distribusi Kategorik')

    # copy variable kategorik
    cat_1 = cat.copy()

    # loop menghapus kolom yang tidak digunakan
    for i in ['week', 'day', 'month','deposit']:
        # jika i ada dalam cat_1
        if i in cat_1:
            # remove i
            cat_1.remove(i)

    # create canvas
    fig = plt.figure(figsize=(20,20))

    # loop histogram
    for idx,i in enumerate(cat_1):
        # urut dari terbanyak
        urut = df[i].value_counts(ascending=False).index
        
        # subplot 3x3
        plt.subplot(3,3,idx+1)
        
        # plot histogram
        ax=sns.countplot(x=df[i],order=urut)

        # add gridline
        plt.grid(True, linestyle = '--', color = 'grey', alpha = 0.3)
        # add title
        plt.title(i)
        # perlakuan kolom job
        if i=='job':
            # rotate x label 90 derajat
            plt.xticks(rotation=90)

        # menghitung panjang tiap bar
        total = float(len(df[i]))

        # loop untuk add persentase tiap kategori
        for p in ax.patches:
            # menghitung persentase per kategori
            percentage = '{:.1f}%'.format(100 * p.get_height() / total)
            
            # menghitung lebar x dan y
            x = p.get_x() + p.get_width() / 2 - 0.05
            y = p.get_height()

            # add persentase per kategori
            ax.annotate(percentage, (x, y), ha='center', va='bottom')

    # show plot
    st.pyplot(fig)

    # insight
    st.write('''
**Status Pernikahan:** Lebih dari 50% nasabah adalah orang yang sudah menikah.

**Jenis Pekerjaan:** Mayoritas nasabah bekerja di bidang manajemen (23%), dan sekitar 50% berpendidikan di tingkat secondary education.

**Tanggungan dan Pinjaman:**

- Kebanyakan nasabah tidak memiliki tanggungan rumah maupun pinjaman lainnya.

- Nasabah yang memiliki tanggungan rumah (53%) dan yang tidak (47%) relatif seimbang.

**Credit Default:** Nasabah tidak pernah mengalami credit default atau kegagalan dalam membayar pinjaman.

**Outcome Kampanye Sebelumnya:** Sebagian besar hasil dari kampanye pemasaran sebelumnya adalah "unknown" (74%), kemungkinan besar karena mayoritas nasabah adalah nasabah baru.

**Keputusan Berdeposit:** Mayoritas nasabah menolak untuk berdeposit, tetapi perbedaannya dengan yang setuju untuk berdeposit relatif seimbang.

Lalu bagaimana dengan hal yang berhubungan dengan waktu?
''')

    # categorik waktu
    cat_2 = ['day', 'week', 'month']

    # Urutan bulan
    month_order = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']

    # Set figure
    fig = plt.figure(figsize=(15,5))

    # Loop untuk setiap kategori
    for idx, i in enumerate(cat_2):
        
        # Jika kolom adalah 'month', urutkan berdasarkan urutan bulan
        if i == 'month':
            df[i] = pd.Categorical(df[i], categories=month_order, ordered=True)
            data_agg = df.groupby(i).size()
        else:
            # Agregasi data untuk week dan day
            data_agg = df.groupby(i).size()
        
        # Subplot 1x3
        plt.subplot(1, 3, idx + 1)
        
        # Plot line plot
        sns.lineplot(x=data_agg.index, y=data_agg.values, marker="o")

        # Tambahkan gridline
        plt.grid(True, linestyle='--', color='grey', alpha=0.3)

        # Tambahkan title
        plt.title(f'Trend of {i}')

    # show plot
    st.pyplot(fig)

    # mengembalikan dtype month ke object
    df['month'] = df['month'].astype(object)

    # insight
    st.write('''
**Kontak terbanyak pada minggu ke-3:**
             
Kontak terbanyak ditujukan oleh bank ke telepon seluler nasabah, pada tanggal 20 atau minggu ke-3, dan/atau bulan Mei. Tingginya kontak pada bulan mei mungkin berhubungan dengan adanya event finansial tertentu.

**Tren Harian & Bulanan tidak memiliki pola:**
             
Melihat dari tren harian dan bulanan tidak menunjukkan adanya tren dalam jumlah kontak. Namun, ketika melihat tren mingguan, ditemukan bahwa awal dari mingggu pertama sampai dengan minggu ke-3 terjadi peningkatan jumlah kontak, sedangkan minggu ke-3 ke-minggu ke-4 terjadi penurunan tren. Hal ini mungkin terjadi karena pada minggu ke-3 biasanya orang-orang yang bekerja menerima gaji sehingga memperbesar kemungkinan nasabah untuk berdeposit.
''')

    # sub judul
    st.write('# Bivariate Analysis')

    # sub judul
    st.write('## Deposit by Job')

    #set figure
    fig = plt.figure(figsize=(7,5))

    # urut dari terbanyak
    urut = df['job'].value_counts(ascending=False).index

    # plot histogram
    ax=sns.countplot(y=df['job'],order=urut,hue=df['deposit'])

    # add gridline
    plt.grid(True, linestyle = '--', color = 'grey', alpha = 0.3)
    # add title
    plt.title(f'Deposit by Job')

    # show plot
    st.pyplot(fig)

    # insight
    st.write('''
**Distribusi Pekerjaan:**
             
Pada grafik terlihat bahwa walaupun top 3 pekerjaan terbanyak dalam data adalah manajemen, blue-collar, dan technician, tidak semuanya menunjukkan jumlah nasabah berdeposit yang lebih tinggi dari yang tidak. Justru pekerjaan pekerjaan yang menunjukkan jumlah nasabah berdeposit lebih besar dari yang tidak adalah pekerjaan pasif seperti pensiunan, pelajar, unemployed ditambah dengan manajemen.

**Nasabah yang tidak aktif bekerja:**
             
Nasabah dengan pekerjaan sebagai pelajar, pensiunan, belum bekerja, dan manajemen secara berturut turut dari yang terbesar menghasilkan persentase keberhasilan lebih dari 50%, sedangkan jenis pekerjaan lainnya dibawah 50%. Melihat bahwa data menunjukkan nasabah yang tidak aktif bekerja memiliki persentase keberhasilan yang cukup tinggi (bahkan pelajar mencapai 74%) menandakan bahwa orang-orang ini lebih bergantung kepada pasive income, sedangkan orang yang bekerja sebagai manajemen biasanya memiliki pengetahuan yang lebih mengenai finansial sehingga cenderung akan berdeposit.
             ''')

    # judul
    st.write('## Deposit by Marital')

    #set figure
    fig = plt.figure(figsize=(7,5))

    # urut dari terbanyak
    urut = df['marital'].value_counts(ascending=False).index

    # plot histogram
    ax=sns.countplot(x=df['marital'],order=urut,hue=df['deposit'])

    # add gridline
    plt.grid(True, linestyle = '--', color = 'grey', alpha = 0.3)
    # add title
    plt.title(f'Deposit by marital')

    # show plot
    st.pyplot(fig)

    # insight
    st.write('''
**Status 'Single':** Lebih cenderung berdeposit dibandingkan dengan status pernikahan lainnya. Hal ini mungkin disebabkan oleh kurangnya tanggungan selain diri sendiri, sehingga memiliki lebih banyak dana yang tersedia untuk berdeposit.

**Status 'Married' dan 'Divorced':**
- Nasabah yang sudah menikah lebih cenderung tidak berdeposit, kemungkinan karena adanya tanggungan keluarga seperti istri dan anak.
- Nasabah yang bercerai menunjukkan jumlah yang relatif seimbang antara yang berdeposit dan yang tidak, namun sedikit lebih banyak yang tidak berdeposit.
             ''')

    # judul
    st.write('## Deposit by Education')

    #set figure
    plt.figure(figsize=(7,5))

    # urut dari terbanyak
    urut = df['education'].value_counts(ascending=False).index

    # plot histogram
    ax=sns.countplot(x=df['education'],order=urut,hue=df['deposit'])

    # add gridline
    plt.grid(True, linestyle = '--', color = 'grey', alpha = 0.3)
    # add title
    plt.title(f'Deposit by education')

    # show plot
    st.pyplot(fig)

    # insight
    st.write('''
**Pendidikan Tingkat Tertiary:**

Nasabah yang memiliki tingkat pendidikan tertinggi (tertiary) menunjukkan persentase yang lebih besar untuk berdeposit dibandingkan dengan tingkat pendidikan lainnya. Hal ini mungkin disebabkan oleh pemahaman yang lebih baik mengenai manfaat deposito yang didapat dari pendidikan yang lebih tinggi.

**Pendidikan Tingkat Secondary dan Primary:**

Untuk tingkat pendidikan secondary, lebih banyak nasabah yang tidak berdeposit dibandingkan dengan yang berdeposit. Hal yang sama berlaku untuk tingkat pendidikan primary, dimana lebih banyak nasabah yang tidak berdeposit.

**Pendidikan Tidak Diketahui (Unknown):**

Nasabah dengan pendidikan yang tidak diketahui lebih cenderung tidak berdeposit.
''')

    # judul
    st.write('## Deposit by Default, Housing & Loan')

    #set figure
    fig = plt.figure(figsize=(8,4))

    # loop histogram
    for idx,i in enumerate(['default', 'housing', 'loan']):
        # urut dari terbanyak
        urut = df[i].value_counts(ascending=False).index
        
        # subplot 1x3
        plt.subplot(1,3,idx+1)
        
        # plot histogram
        ax=sns.countplot(x=df[i],order=urut,hue=df['deposit'])

        # add gridline
        plt.grid(True, linestyle = '--', color = 'grey', alpha = 0.3)
        # add title
        plt.title(f'deposit by {i}')
        # perlakuan kolom job
        if i=='job':
            # rotate x label 90 derajat
            plt.xticks(rotation=90)

    # show
    st.pyplot(fig)

    # insight
    st.write('''
**Default:**

Nasabah yang tidak pernah mengalami gagal bayar (default) cenderung lebih stabil secara finansial dan lebih mungkin untuk berdeposit. Walaupun nasabah yang tidak berdeposit lebih banyak, mereka yang tidak pernah mengalami gagal bayar menunjukkan kecenderungan lebih tinggi untuk berdeposit.

**Housing:**

Nasabah yang tidak memiliki tanggungan rumah lebih cenderung untuk berdeposit. Ini mungkin karena mereka memiliki lebih banyak dana yang tersedia tanpa beban cicilan rumah.

**Loan:**

Mirip dengan default, nasabah yang tidak memiliki pinjaman cenderung lebih stabil secara finansial dan lebih mungkin untuk berdeposit. Walaupun jumlah nasabah yang tidak berdeposit lebih banyak, mereka yang tidak memiliki pinjaman menunjukkan kecenderungan lebih tinggi untuk berdeposit.
''')

    # judul
    st.write('## Deposit by Contact')

    #set figure
    fig = plt.figure(figsize=(7,5))

    # urut dari terbanyak
    urut = df['contact'].value_counts(ascending=False).index

    # plot histogram
    ax=sns.countplot(x=df['contact'],order=urut,hue=df['deposit'])

    # add gridline
    plt.grid(True, linestyle = '--', color = 'grey', alpha = 0.3)
    # add title
    plt.title(f'Deposit by contact')

    # show
    st.pyplot(fig)

    # insight
    st.write('''
**Telepon Seluler lebih efektif:**
             
Nasabah yang dihubungi melalui telepon seluler lebih mungkin berdeposit, mungkin karena mereka lebih muda dan lebih mengikuti perkembangan teknologi.
''')

    # judul
    st.write('## Deposit by Poutcome')

    #set figure
    fig = plt.figure(figsize=(7,5))

    # urut dari terbanyak
    urut = df['poutcome'].value_counts(ascending=False).index

    # plot histogram
    ax=sns.countplot(x=df['poutcome'],order=urut,hue=df['deposit'])

    # add gridline
    plt.grid(True, linestyle = '--', color = 'grey', alpha = 0.3)
    # add title
    plt.title(f'Deposit by poutcome')

    # show
    st.pyplot(fig)

    # insight
    st.write('''

- Nasabah yang memilih berdeposit pada kampanye sebelumnya cenderung akan melakukannya lagi.
- Nasabah yang tidak berdeposit pada kampanye sebelumnya dan yang memilih lainnya juga menunjukkan kecenderungan untuk berdeposit pada kampanye kali ini, namun perbedaannya tidak signifikan dengan nasabah yang menolak berdeposit.

Hasil ini menguatkan bahwa outcome dari kampanye sebelumnya dapat mempengaruhi keputusan nasabah untuk berdeposit pada kampanye yang sedang berjalan.
''')

    # judul
    st. write('## Deposit by Week')

    # Agregasi data untuk setiap kategori
    data_agg = df.groupby(['week', 'deposit']).size().reset_index(name='count')

    # Plot line plot
    sns.lineplot(data=data_agg, x='week', y='count', marker="o", hue='deposit')

    # Tambahkan gridline
    plt.grid(True, linestyle='--', color='grey', alpha=0.3)

    # Tambahkan title
    plt.title('Trend of Week')

    # show
    st.pyplot(fig)

    # insight
    st.write('''
Grafik ini memberikan pemahaman tentang kapan waktu terbaik untuk menghubungi nasabah agar lebih efektif dalam mengajak mereka untuk berdeposit.

- Meski ada banyak kontak pada minggu ke-3, efektivitasnya dalam mendorong nasabah untuk berdeposit tampaknya lebih rendah dibandingkan minggu pertama.
- Minggu pertama mungkin menjadi waktu yang lebih efektif untuk menghubungi nasabah, mungkin karena mereka lebih responsif di awal bulan atau minggu.
''')

    #judul
    st.write('## Korelasi Antar Fitur Numerik')

    # figure
    fig = plt.figure(figsize=(7,7))

    # plot
    sns.heatmap(df[num].corr(method='spearman'),annot=True,fmt='.2f',square=True,cmap='coolwarm')

    # show
    st.pyplot(fig)

    # insight
    st.write('''
Fitur 'pdays' memiliki korelasi positif yang sangat kuat dengan fitur 'previous', dimana semakin banyak kontak yang dilakukan sebelum kampanye, maka semakin banyak jumlah hari berlalu sejak kontak terakhir.
''')
    

    #judul
    st.write('## Kesimpulan')

    # insight
    st.write('''
Berdasarkan analisis data, dapat disimpulkan:
1. **Usia dan Pekerjaan:**

Sebagian besar nasabah berusia antara 30-50 tahun, menunjukkan bahwa mereka berada di usia produktif. Nasabah yang memiliki pekerjaan seperti pelajar, pensiunan, unemployed, dan manajemen memiliki persentase berdeposit lebih tinggi, menunjukkan bahwa mereka lebih mungkin untuk berdeposit dibandingkan dengan pekerjaan lainnya.

2. **Status Pernikahan:**

Nasabah yang masih single cenderung lebih banyak yang berdeposit dibandingkan dengan yang sudah menikah atau bercerai, kemungkinan karena mereka memiliki tanggungan yang lebih sedikit.

3. **Pendidikan:**

Nasabah dengan pendidikan tingkat tertiary lebih cenderung untuk berdeposit, mungkin karena pemahaman mereka yang lebih baik tentang manfaat deposito.

4. **Stabilitas Finansial:**

Nasabah yang tidak pernah mengalami credit default, tidak memiliki tanggungan rumah, dan tidak memiliki pinjaman lebih cenderung berdeposit karena mereka dianggap lebih stabil secara finansial.

5. **Metode Kontak:**

Nasabah yang dihubungi melalui telepon seluler lebih cenderung berdeposit, mungkin karena mereka lebih muda dan lebih mengikuti perkembangan teknologi.

6. **Outcome Kampanye Sebelumnya:**

Nasabah yang berdeposit pada kampanye sebelumnya cenderung akan melakukannya lagi, menunjukkan bahwa pengalaman positif dari kampanye sebelumnya berpengaruh.

7. **Waktu Kontak:**

Meskipun kontak terbanyak terjadi pada minggu ke-3, lebih banyak nasabah yang berdeposit terjadi pada minggu pertama, menunjukkan bahwa awal bulan atau minggu mungkin waktu yang lebih efektif untuk menghubungi nasabah.

**Model Prediksi:**
Peningkatan precision dari 75% ke 82% pada data training, dan dari 74% ke 79% pada data testing, menunjukkan bahwa tuning parameter membawa peningkatan yang signifikan dalam performa model.

Model prediksi dengan precision di atas 70% seperti yang diharapkan dalam problem statement berhasil dicapai dengan KNN.
''')
    

    #judul
    st.write('## Saran')

    # insight
    st.write('''
1. **Targeting Demografi:** Fokus pada nasabah usia produktif (30-50 tahun) dan pekerjaan dengan persentase berdeposit tinggi seperti manajemen, pelajar, pensiunan, dan unemployed.

2. **Pendidikan dan Edukasi:** Kampanye edukatif mengenai manfaat deposito, terutama bagi nasabah dengan pendidikan tinggi (tertiary).

3. **Stabilitas Finansial:** Prioritaskan nasabah tanpa tanggungan rumah, pinjaman pribadi, dan tidak pernah mengalami credit default.

4. **Metode Kontak:** Gunakan telepon seluler sebagai metode kontak utama.

5. Penggunaan Data Historis: Targetkan kembali nasabah yang sukses dalam kampanye sebelumnya.

6. **Timing yang Tepat:** Hubungi nasabah di awal bulan atau minggu pertama.

7. **Penawaran Khusus:** Berikan penawaran promosi seperti suku bunga lebih tinggi atau hadiah menarik.
''')
    

if __name__ == '__main__':
    run()