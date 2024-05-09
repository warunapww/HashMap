import unittest
from hashmap import HashMap

class TestHashMap(unittest.TestCase):
  """Unit tests for HashMap
  """

  def test_create(self):
    map = HashMap()
    self.assertIsNotNone(map)
    self.assertEqual(map.capacity, 30)

  def test_insert(self):
    map = HashMap()
    key = "key1"
    value = 99
    map.set(key, value)
    val = map.get(key)
    self.assertEqual(value, val)

  def test_set(self):
    map = HashMap()
    key = "key1"
    value = 99
    map.set(key, value)
    value = 10
    map.set(key, value)
    val = map.get(key)
    self.assertEqual(value, val)

  def test_remove(self):
    map = HashMap()
    key = "key1"
    value = 99
    map.set(key, value)
    map.delete(key)
    val = map.get(key)
    self.assertIsNone(val)

  def test_get(self):
    map = HashMap()
    key = "key1"
    value = 99
    map.set(key, value)
    val = map.get(key)
    self.assertEqual(value, val)

  def test_hash(self):
    map = HashMap()
    index = map._hash("test1")
    self.assertTrue(index < map.capacity and index >= 0)

  def test_same_index(self):
    """
    """
    strList = [ '8e.x%f3_,4ih$u. R4w,;\x0b\x0b?C,,\\tmsXo', 
                'Q<s;X:Im5}mi)Da6*[O7\x0bC i{c-#^\\~l(v\x0bpkqLCcpd*d5(n.hhi`j{v(rvXICJ/0T',
                '\tgxq3^A2AVC4(+=sWJ7NR(n6sd0qT3"N@]"1PElF(M{s_l\nqD!e-&VDsA \x0c`BIeB\x0cCgQ^u{<Fq[',
                'j.,|oc5gZxu4w!\tP4',
                "B@^:du9yC-Z==J_1vLIm-\n|gQ$!5T%l'r-cd`k4QMJu['iwvs}}$OKyx\rGtQN",
                'u#~Vr*\\Aq>>F+J3 uZA$ a',
                ' KK/|XyUYgtA[Nc&XG\n\r\r_ey\x0by x\x0cP_"cJes&E(mE',
                'yl1:e',
                "g'J<)'l\x0b{`sSOtJ>=w7/\x0b[(gb8Wz'%u?jhVaJ0$PJbqfK",
                'k\nP.N#_ia{Ti~s(tguz<8x/n-PqNH)g\x0bwJhq;_K/TbI\x0bra<+hnN\x0cdyHGN|R"Oj`>RDpY8DX>>IL2Ls\'n\tiVFVO',
                "V_$rPO}8X<PY*.T'd-=wrPd9a\x0c4O%B_6IvbVB~$ulQ_1oijwjaO][t$PNZif=o*XWK94AZPIAt\r",
                '`83KbcTD5*="FJ)0Q\'eul"EO0?Z>lzQT(oQ ZPZWv9Ob;/E1a\nMA@%WU;WGyi\\tqc}I0f=4',
                'X\rH/^"|Ic',
                '_#Ztuf5yJ~I%#[}K3n/UJ2LJw!KpYg\r@U@r"aB^Z;e9',
                "\\D(lTZ;'~5)qE&a}8\x0c&Wbf|6Rq1R%_ONFJUwd{g_W~TrIrs\t11aQ\rxryr}\x0bi7COly3'-4n",
                'oh_O#I_a<^xX5|}jYu,Ju6/D3yzS1Mo?k0_wS%|Z/;s"jO?2z\x0c70',
                '?|cJ9~<\x0czlz\t$MCXHRLc<$00v\x0cM/1',
                'TlCsNDEJql?9k|ky+YN*&$NCd#+qWG9*O)6]ZRSP7JL0/I4*T7JzZT#$*\rb|#',
                '#PpFt:P0\t(?sy+D0U\'q\n\'V\\m9QS\t(T"Oh %l;hy~P:(vQ#%c:tr5f4zs;Js4\ni',
                'vsB9sQSy-sWH1C#@%fyl\n4RY.g\x0b_Y\'^\rL;<FA"^C.Gei-DW[g/)5_&qmZqoC\t*f+k~e;',
                'KO!,qoXdo6U5[{x3wj@m{:2>E7|5\r]mUeS`',
                'Db8rg1\\cF{Vo?:f;3\x0b|Ou(p)@!\r8|iQe:8\teOs4NHCi;5tw=-v,',
                '^dVHReHRa{$`q&r9|6vAeh+<CYJrJW@FOEc Ma~@oW\tHEN\x0b3Js5|N|blI%g\x0cegHR[jr4>!x!z0N',
                '}VW0=% DL (\\j46YS9l2N)\\KtIvV2:\r(>P)`9"\\N^y`J;GlH6LEbT7.?',
                'L gzsQjA^wJG\x0crs0h:v\tz/,.M2*lI\x0cC$|1\\lB?}5\x0b\n"uS\rvH',
                "mi$PsnCl\x0cx\x0bI']R",
                '\x0b/N53wMcAL#0\'";81r21\x0biaTPp@)]7',
                '4j\ri8I"\\W:E\x0b%n"8va\x0c#OErDw7K>Lk]A3E51KTG__1(6vjmC<u^q NvSOj.q;M',
                '1 Qd\n_EbL8%ZL#|FSfK2CY&.fA.p<\x0ba?\rTkJ\x0b6\td|@&AJ%G}B~p-KdD\x0c.;H!8704euha)GWtN',
                "5/+qfvos]Ihr3S%+'",
                'iVT@VpEV.Eu~c1)pKbtl"j H\tswy|22cA4*Tt$p\njK&1w?*S\x0bpW:kxb~<gNnzla3hiCPiv:iG>Sl[._^\n-zDu\n"*Jdee3']

if __name__ == '__main__':
    unittest.main()
