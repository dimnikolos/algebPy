LIBRARY IEEE;
USE IEEE.STD_LOGIC_1164.ALL;
USE IEEE.STD_LOGIC_ARITH.ALL;
USE IEEE.STD_LOGIC_UNSIGNED.ALL;

entity clock is
port ( signal clock, reset : out std_logic);
end entity clock;

architecture behavior of clock is 
begin
	reset <= '1', '0' after 75 ns;
    process
        begin
        -- generate clock
          clock <= '0', '1' after 50 ns;
          wait for 100 ns;
         end process; 

end architecture behavior;
    
