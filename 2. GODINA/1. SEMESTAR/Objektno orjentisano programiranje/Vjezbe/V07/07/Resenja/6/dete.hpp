#ifndef DETE_HPP_INCLUDED
#define DETE_HPP_INCLUDED

#include "putnik.hpp"

class PutnikDete : public Putnik
{
private:
    int mbRoditelja;
public:
    PutnikDete():Putnik(), mbRoditelja(1234546548135) {}
    PutnikDete(int bk, VrstaKarte vk, const DinString& maticniBroj, const DinString& imePutnika, int mbR): Putnik(bk, vk, maticniBroj, imePutnika), mbRoditelja(mbR) {}
    PutnikDete(const Putnik& p, int mbR): Putnik(p), mbRoditelja(mbR) {}

    DinString toString() const
    {
        return "Dete " + ime + " " + mb;
    }
};

#endif // DETE_HPP_INCLUDED
