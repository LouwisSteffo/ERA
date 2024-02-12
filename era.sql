-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Feb 12, 2024 at 03:07 AM
-- Server version: 10.4.19-MariaDB
-- PHP Version: 8.0.7

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `era`
--

-- --------------------------------------------------------

--
-- Table structure for table `alembic_version`
--

CREATE TABLE `alembic_version` (
  `version_num` varchar(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `alembic_version`
--

INSERT INTO `alembic_version` (`version_num`) VALUES
('6faaa07dd20d');

-- --------------------------------------------------------

--
-- Table structure for table `ekspedisi`
--

CREATE TABLE `ekspedisi` (
  `id` int(11) NOT NULL,
  `nama_ekspedisi` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `kupon`
--

CREATE TABLE `kupon` (
  `id` int(11) NOT NULL,
  `nama_kupon` varchar(100) NOT NULL,
  `harga_kupon` int(11) NOT NULL,
  `gambar_kupon` varchar(100) NOT NULL,
  `jumlah_kupon` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `limbah_elektronik`
--

CREATE TABLE `limbah_elektronik` (
  `id` int(11) NOT NULL,
  `nama_limbah` varchar(100) NOT NULL,
  `gambar_limbah` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `lokasi`
--

CREATE TABLE `lokasi` (
  `id` int(11) NOT NULL,
  `nama_lokasi` varchar(100) NOT NULL,
  `alamat_lokasi` varchar(100) NOT NULL,
  `waktu_buka` datetime NOT NULL,
  `waktu_tutup` datetime NOT NULL,
  `gambar_lokasi` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `pengguna`
--

CREATE TABLE `pengguna` (
  `id` int(11) NOT NULL,
  `username` varchar(20) NOT NULL,
  `email` varchar(120) NOT NULL,
  `nomor_telepon` varchar(20) NOT NULL,
  `foto_profil` varchar(100) DEFAULT NULL,
  `alamat` varchar(100) NOT NULL,
  `poin` int(11) NOT NULL,
  `password` varchar(300) NOT NULL,
  `nama_pengguna` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `pengguna`
--

INSERT INTO `pengguna` (`id`, `username`, `email`, `nomor_telepon`, `foto_profil`, `alamat`, `poin`, `password`, `nama_pengguna`) VALUES
(1, 'admin', 'lou@gmail.com', '08123456789', 'default.jpg', 'Jl. Kebon Jeruk No. 1', 0, '$2b$12$0QstC6SJrvT2roarZ3M1W.0sRS7Gn8BY/34c.7YKSdIt.nMYA.gcq', 'Lous');

-- --------------------------------------------------------

--
-- Table structure for table `transaksi_penjemputan`
--

CREATE TABLE `transaksi_penjemputan` (
  `id` int(11) NOT NULL,
  `id_pengguna` int(11) NOT NULL,
  `id_ekspedisi` int(11) NOT NULL,
  `id_lokasi` int(11) NOT NULL,
  `berat_limbah` int(11) NOT NULL,
  `status_transaksi` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `alembic_version`
--
ALTER TABLE `alembic_version`
  ADD PRIMARY KEY (`version_num`);

--
-- Indexes for table `ekspedisi`
--
ALTER TABLE `ekspedisi`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `kupon`
--
ALTER TABLE `kupon`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `limbah_elektronik`
--
ALTER TABLE `limbah_elektronik`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `lokasi`
--
ALTER TABLE `lokasi`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `pengguna`
--
ALTER TABLE `pengguna`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`),
  ADD UNIQUE KEY `nomor_telepon` (`nomor_telepon`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `transaksi_penjemputan`
--
ALTER TABLE `transaksi_penjemputan`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_ekspedisi` (`id_ekspedisi`),
  ADD KEY `id_lokasi` (`id_lokasi`),
  ADD KEY `id_pengguna` (`id_pengguna`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `ekspedisi`
--
ALTER TABLE `ekspedisi`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `kupon`
--
ALTER TABLE `kupon`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `limbah_elektronik`
--
ALTER TABLE `limbah_elektronik`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `lokasi`
--
ALTER TABLE `lokasi`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `pengguna`
--
ALTER TABLE `pengguna`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `transaksi_penjemputan`
--
ALTER TABLE `transaksi_penjemputan`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `transaksi_penjemputan`
--
ALTER TABLE `transaksi_penjemputan`
  ADD CONSTRAINT `transaksi_penjemputan_ibfk_1` FOREIGN KEY (`id_ekspedisi`) REFERENCES `ekspedisi` (`id`),
  ADD CONSTRAINT `transaksi_penjemputan_ibfk_2` FOREIGN KEY (`id_lokasi`) REFERENCES `lokasi` (`id`),
  ADD CONSTRAINT `transaksi_penjemputan_ibfk_3` FOREIGN KEY (`id_pengguna`) REFERENCES `pengguna` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
