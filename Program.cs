namespace Random_Route_new
{
    internal class Program
    {
        static void Main(string[] args)
        {
            string nyers = File.ReadAllText("source.txt");
            string[] nyers2 = nyers.Split("\n\n");
            string[] index = new string[nyers2.Length];   //a város-út tömb indexeinek listája
            string[] name = new string[101 * (nyers2.Length)];  //a város-út tömb városainak/útjainak listája, olyan módon, hogy ((index * 100) + város/út sorszáma)
            int x = 0;
            for (int i = 0; i < nyers2.Length; i++)
            {
                string[] splitted = nyers2[i].Split("\n");
                index[i] = splitted[0];
                for (int j = 1; j < splitted.Length; j++)
                {
                    name[(100*i)+x] = splitted[j];
                    x++;
                }
                x = 0;
            }
            Console.Write("Állomások száma: ");
            int állomás = Convert.ToInt32(Console.ReadLine());
            Console.Write("Induló település: ");
            string aktuális = Console.ReadLine();
            int aktid = 0;
            for (int i = 0; i < index.Length; i++)  //az induló település indexének id-jét az "aktid"-be menti
            {
                if (index[i] == aktuális)
                {
                    aktid = i;
                    Console.WriteLine(index[i]);
                }
            }
            Random rnd = new Random();
            for (int i = 1; i <= állomás; i++)
            {
                for (int j = 100*aktid; j < 100*(aktid+1); j++) //megnézi, mennyi út vagy város van az adott index alatt
                {
                    if (name[j] == null)
                    {
                        x = j - (100 * aktid);
                        break;
                    }
                }
                int y = rnd.Next(x);
                aktuális = name[(100 * aktid) + y];
                if (aktuális == null)
                    break;
                Console.WriteLine(aktuális);
                for (int j = 0; j < index.Length; j++)
                {
                    if (index[j] == aktuális)
                        aktid = j;
                }    
            }
        }
    }
}