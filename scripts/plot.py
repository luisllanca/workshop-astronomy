import numpy as np
import matplotlib.pyplot as plt

def plot_light_curve(lc,period,fold=False):
    mjds,mags,errs,bands = lc
    for band,band_name in zip(np.unique(bands),['g','r']):
        mask = bands == band
        mjd = mjds[mask]
        mag = mags[mask]
        err = errs[mask]
        if fold:
            phase = np.mod(mjd,period)/period
            plt.errorbar(phase,mag,err,fmt=".",label=band_name,c=band_name)
        else:
            plt.errorbar(mjd,mag,err,fmt=".",label=band_name,c=band_name)
    plt.xlabel("Time [MJD]")
    plt.ylabel("Magnitude")
    plt.legend()
    plt.gca().invert_yaxis()
import matplotlib.pyplot as plt

def plot_smoothed_matplotlib(pha_interp, mag_interp, err_interp, width=6):
    plt.figure(figsize=(width, 4))

    # Banda g
    plt.plot(pha_interp, mag_interp[0], label='g', color='g', alpha=0.6)
    plt.fill_between(pha_interp,
                     mag_interp[0] - err_interp[0],
                     mag_interp[0] + err_interp[0],
                     color='g', alpha=0.25)

    # Banda r
    plt.plot(pha_interp, mag_interp[1], label='r', color='r', alpha=0.6)
    plt.fill_between(pha_interp,
                     mag_interp[1] - err_interp[1],
                     mag_interp[1] + err_interp[1],
                     color='r', alpha=0.25)

    plt.xlabel("Phase")
    plt.ylabel("Magnitude")
    plt.gca().invert_yaxis()
    plt.legend()
    plt.tight_layout()
    plt.show()
