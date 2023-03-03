namespace Random_Route_new
{
	internal class Program
	{
		static void Main(string[] args)
		{
			string be = File.ReadAllText("source/HU road.txt");
			string[] be2 = be.Split("\n\n");
			string[,] tömb = new string[be2.Length, 101 * be2.Length];
			for (int i = 0; i < be2.Length; i++)
			{
				string[] splitted = be2[i].Split("\n");
				tömb[0, i] = splitted[0];
				for (int j = 1; j < splitted.Length; j++)
				{
					tömb[1, (100 * i) + (j - 1)] = splitted[j];
				}
			}
			Console.Write("Állomások száma: ");
			int állomás = Convert.ToInt32(Console.ReadLine());
			Console.Write("Induló település: ");
			string aktuális = Console.ReadLine();
			int aktid = 0;
			for (int i = 0; i < tömb.GetLength(0); i++)  //az induló település indexének id-jét az "aktid"-be menti
			{
				if (tömb[0, i] == aktuális)
				{
					aktid = i;
					Console.WriteLine(tömb[0, i]);
				}
			}
			Random rnd = new Random();
			int x = 0;
			for (int i = 1; i <= állomás; i++)
			{
				for (int j = 100 * aktid; j < 100 * (aktid + 1); j++) //megnézi, mennyi út vagy város van az adott index alatt
				{
					if (tömb[1, j] == null)
					{
						x = j - (100 * aktid);
						break;
					}
				}
				int y = rnd.Next(x);
				aktuális = tömb[1, (100 * aktid) + y];
				if (aktuális == null)
					break;
				Console.WriteLine(aktuális);
				for (int j = 0; j < tömb.GetLength(0); j++)
				{
					if (tömb[0, j] == aktuális)
						aktid = j;
				}
			}
		}
	}
}
