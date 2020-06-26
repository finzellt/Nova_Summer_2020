from astroquery.eso import Eso
eso = Eso()
eso.login('pks137', store_password=True)
eso.ROW_LIMIT = 500

#IMPORT SIMBAD#
from astroquery.simbad import Simbad
sim = Simbad()
simbad_nova = sim.query_object("V1369 Cen")

from astropy.coordinates import SkyCoord
from astropy import units as u

# true_nova = SkyCoord('13h54m45.3629s', '-59d09m04.170s', frame = 'icrs')

true_coord = SkyCoord(simbad_nova['RA'], simbad_nova['DEC'], unit=(u.hourangle, u.deg))

uves = eso.query_surveys('UVES', target = 'nova Cen 2013') 

# , wavelength = '373.2' and '500', date_obs = '2015-04-06')#

for x in range(len(uves)):
    RA = uves['RA'][x]
    Dec = uves['DEC'][x]
    uves_coord = SkyCoord(ra = RA*u.degree, dec = Dec*u.degree)
    sep = true_coord.separation(uves_coord)
    if sep.arcsecond <= 10 and uves['SNR'][x] > 5:
        print(uves['Object', 'ARCFILE', 'SNR'][x])



    



