#ifndef ZICARA_HPP_INCLUDED
#define ZICARA_HPP_INCLUDED

#include "putnik.hpp"
#include "list.hpp"

enum StanjeZicare { OTVORENA, ZATVORENA };

template <VrstaKarte SEZONA, int BROJ_SEDISTA, int INTERVAL>
class Zicara
{
private:
    List<Putnik*> putnici;
    StanjeZicare stanje;
    int ukupnoVoznji, ukupnoMinuta;
public:
    Zicara():stanje(ZATVORENA), ukupnoVoznji(0), ukupnoMinuta(0) {}

    void otvori()
    {
        stanje = OTVORENA;
        ukupnoVoznji = 0;
        ukupnoMinuta = 0;
    }

    void zatvori()
    {
        stanje = ZATVORENA;
        putnici.clear();
    }

    bool putnikNijeURedu(const Putnik& putnik)
    {
        Putnik* p;
        for(int i=1; i<=putnici.size(); i++)
        {
            putnici.read(i, p);
            if(putnik.getMb()==p->getMb())
                return false;
        }
        return true;
    }

    void dodajPutnika(Putnik* p)
    {
        if(putnikNijeURedu(*p))
            putnici.add(putnici.size()+1, p);
    }

    int brojPutnika() const
    {
        return putnici.size();
    }

    void ukloniPutnikeIzReda(int brojPutnikaZaUklanjanje)
    {
        while(brojPutnikaZaUklanjanje--)
            putnici.remove(1);
    }

    void preveziTuru()
    {
        if(stanje == ZATVORENA)
            return;

        int brojPrevezenihPutnika = 0;
        int brojPutnikaSaNeispravnimKartama = 0;
        Putnik *p;

        for(int i=1; i <= putnici.size(); i++)
        {
            putnici.read(i, p);

            if(p->getVrstaKarte() == SEZONA)
                brojPrevezenihPutnika++;
            else
                brojPutnikaSaNeispravnimKartama++;

            if(brojPrevezenihPutnika == BROJ_SEDISTA)
                break;
        }

        ukupnoVoznji += brojPrevezenihPutnika;
        ukupnoMinuta += INTERVAL;
        ukloniPutnikeIzReda(brojPrevezenihPutnika + brojPutnikaSaNeispravnimKartama);
    }

    friend ostream& operator<<(ostream& os, const Zicara<SEZONA, BROJ_SEDISTA, INTERVAL>& z)
    {
        os << "Sezona: " << z.getSezona() << endl;
        os << "Broj sedista: " << BROJ_SEDISTA << endl;
        os << "Trajanje jedne voznje: " << INTERVAL << endl;
        os << "Stanje: " << (z.stanje == 1 ? "ZATVORENA" : "OTVORENA" )<< endl;
        os << "Ukupan broj voznji: " << z.ukupnoVoznji << endl;
        os << "Radno vreme(sati): " << z.getRadnoVremeUSatima() << endl;
        os << "Broj putnika u redu: " << z.putnici.size() << endl;

        if(z.putnici.size())
        {
            os << "Lista putnika u redu:" << endl;
            Putnik *p;
            for(int i=1; i <= z.putnici.size(); i++)
            {
                z.putnici.read(i, p);
                os << *p << endl;
            }
        }

        return os;
    }

    double getRadnoVremeUSatima() const
    {
        return (double)ukupnoMinuta / 60;
    }

    DinString getSezona() const
    {
        switch(SEZONA)
        {
        case(LETO):
            return "LETO";
        case(SKI):
            return "SKI";
        case(SKI_OPENING):
            return "SKI OPENING";
        }

    }
};

#endif // ZICARA_HPP_INCLUDED
