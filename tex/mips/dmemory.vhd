-- Dmemory module (implements the data memory for MIPS)
LIBRARY IEEE;
USE IEEE.STD_LOGIC_1164.ALL;
USE IEEE.STD_LOGIC_ARITH.ALL;
USE IEEE.STD_LOGIC_SIGNED.ALL;
LIBRARY altera_mf;
USE altera_mf.altera_mf_components.ALL;
ENTITY dmemory IS PORT( read_data : OUT STD_LOGIC_VECTOR( 31 DOWNTO 0 );
						address : IN STD_LOGIC_VECTOR( 7 DOWNTO 0 );
						write_data : IN STD_LOGIC_VECTOR( 31 DOWNTO 0 ); 
						MemRead, Memwrite : IN STD_LOGIC;
						clock, reset : IN STD_LOGIC );
END dmemory;
ARCHITECTURE behavior OF dmemory IS
SIGNAL write_clock : STD_LOGIC;
BEGIN 
data_memory: altsyncram GENERIC MAP ( operation_mode => "SINGLE_PORT", 
	width_a => 32, 
	widthad_a => 8, 
	lpm_type => "altsyncram", 
	outdata_reg_a => "UNREGISTERED", 
	-- -- Reads in mif file for initial data memory values 
	init_file => "dmemory.mif", 
	intended_device_family => "Cyclone")
PORT MAP ( wren_a => memwrite, 
		clock0 => write_clock, 
		address_a => address, 
		data_a => write_data, 
		q_a => read_data ); 
-- Load memory address & data register with write clock 
write_clock <= NOT clock;
END behavior;