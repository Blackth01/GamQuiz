CREATE DATABASE IF NOT EXISTS `gamquiz` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `gamquiz`;

-- --------------------------------------------------------

--
-- Table structure for table `jogadores`
--

CREATE TABLE `jogadores` (
  `id` int(11) NOT NULL,
  `username` varchar(15) NOT NULL,
  `senha` varchar(15) NOT NULL,
  `pontos` int(11) NOT NULL,
  `pontos_hoje` int(11) DEFAULT NULL,
  `pontos_matematica` int(11) DEFAULT NULL,
  `p_hoje_matematica` int(11) DEFAULT NULL,
  `token` varchar(32) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


--
-- Table structure for table `perguntas`
--

CREATE TABLE `perguntas` (
  `id` int(11) NOT NULL,
  `texto` text NOT NULL,
  `resposta` varchar(1) DEFAULT NULL,
  `alt_A` text NOT NULL,
  `alt_B` text NOT NULL,
  `alt_C` text NOT NULL,
  `alt_D` text NOT NULL,
  `tipo` char(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Table structure for table `versao`
--

CREATE TABLE `versao` (
  `id` int(11) NOT NULL,
  `valor` decimal(6,2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Indexes for table `jogadores`
--
ALTER TABLE `jogadores`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `perguntas`
--
ALTER TABLE `perguntas`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `versao`
--
ALTER TABLE `versao`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for table `jogadores`
--
ALTER TABLE `jogadores`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1;
--
-- AUTO_INCREMENT for table `perguntas`
--
ALTER TABLE `perguntas`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1;
--
-- AUTO_INCREMENT for table `versao`
--
ALTER TABLE `versao`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1;