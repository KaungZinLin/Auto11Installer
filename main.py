# Imports
from tkinter import *
from tkinter import messagebox
import pyttsx3
import webbrowser

# Functions
def about_win11():
    def open_site():
        webbrowser.open("https://www.microsoft.com/en-us/windows/windows-11")

    def read_out():
        try:
            pyttsx3.speak("Windows 11 is the newest version of the Microsoft Windows operating system that was launched on October 5, 2021. It is meant to offer users a more modern and user-friendly experience than its predecessor, Windows 10.")
        except:
            messagebox.showerror("Error!", "Error: Cannot Read Out!")

    aw11_window = Toplevel()
    aw11_window.title("About Windows 11")
    aw11_window.resizable(False, False)
    aw11_window.config(padx=25, pady=25)

    # Label
    aw11_label = Label(aw11_window, text="About Windows 11", font=('Areal', 25))
    aw11_label.grid(row=0, column=0)

    about_text = "\nWindows 11 is the newest version of the Microsoft Windows operating system that was launched on October 5, 2021. \nIt is meant to offer users a more modern and user-friendly experience than its predecessor, Windows 10."
    # about_text += "\n\nWindows 11 includes several new features, such as a redesigned Start menu, improved virtual desktops, and new customization options for the taskbar and desktop."
    # about_text += "\n\nIt also comes with several enhancements to performance and security, including better support for touch and pen input, improved virtualization capabilities, and enhanced support for biometric authentication."

    about_win11_sw_label = Label(aw11_window, text=about_text)
    about_win11_sw_label.grid(row=1, column=0)

    placeholder_label_2 = Label(aw11_window, text="")
    placeholder_label_2.grid(row=2, column=0)
    # Buttons
    open_site_button = Button(aw11_window, text="Open Site", command=open_site)
    open_site_button.grid(row=3, column=0)

    read_out_button = Button(aw11_window, text="Read Out", command=read_out)
    read_out_button.grid(row=4, column=0)

def system_requirements():
    def open_site():
        webbrowser.open("https://www.microsoft.com/en-us/windows/windows-11-specifications#table1")

    def read_out():
        messagebox.showinfo("!WIP!", "!WIP! - this feature is still in WORK IN PROGRESS. USE IT AT YOUR OWN RISK!")
        try:
            pyttsx3.speak("System requirements The minimum system requirements are necessary for installing Windows 11 on a PC. \nFailure to meet these requirements may result in an inability to install Windows 11, necessitating the purchase of a new PC. \n\nIndividuals can check with the OEM or use the PC Health Check app if their device is already running Windows 10 to verify if the device meets the requirements. \nIt should be noted that the app does not check for graphics card or display requirements since most compatible devices would already meet those requirements. Processor - 1 gigahertz (GHz) or faster with 2 or more cores on compatible 64-bit processor or System on a Chip (SoC). RAM - 4 gigabyte (GB). Storage - 64 GB or larger storage device. System firmware - UEFI, Secure Boot capable. TPM - TPM version 2.0. Graphics card - Compatible with DirectX 12 or later with WDDM 2.0 driver. Display - High definition (720p) display that is greater than 9” diagonally, 8 bits per color channel.")
        except:
            messagebox.showerror("Error!", "Error: Cannot read out!")

    sq_window = Toplevel()
    sq_window.title("System Requirements")
    sq_window.resizable(False, False)
    sq_window.config(padx=20, pady=20)

    # Label
    system_requirement_label = Label(sq_window, text="System Requirements", font=('Areal', 25))
    system_requirement_label.grid(row=0, column=0)

    about_sq_label = Label(sq_window,text="\nThe minimum system requirements are necessary for installing Windows 11 on a PC. \nFailure to meet these requirements may result in an inability to install Windows 11, necessitating the purchase of a new PC. \n\nIndividuals can check with the OEM or use the PC Health Check app if their device is already running Windows 10 to verify if the device meets the requirements. \nIt should be noted that the app does not check for graphics card or display requirements since most compatible devices would already meet those requirements.")
    about_sq_label.grid(row=1, column=0, sticky='W')

    cpu_label = Label(sq_window, text="\nCPU - 1 gigahertz (GHz) or faster with 2 or more cores on a compatible 64-bit processor or System on a Chip (SoC).", font=('Areal', 15))
    cpu_label.grid(row=2, column=0)

    ram_label = Label(sq_window, text="RAM - 4 gigabyte (GB).", font=('Areal', 15))
    ram_label.grid(row=3, column=0)

    storage_label = Label(sq_window, text="Storage - 64 GB or larger storage device", font=('Areal', 15))
    storage_label.grid(row=4, column=0)

    firmware_label = Label(sq_window, text="System firmware - (UEFI) Secure Boot capable. Check here for information on how your PC might be able to meet this requirement.", font=('Areal', 15))
    firmware_label.grid(row=5, column=0)

    tpm_label = Label(sq_window, text="TPM - TPM v2.0.", font=('Areal', 15))
    tpm_label.grid(row=6, column=0)

    gpu_label = Label(sq_window, text="GPU - Compatible with DirectX 12 or later with WDDM 2.0 driver.", font=('Areal', 15))
    gpu_label.grid(row=7, column=0)

    display_label = Label(sq_window, text="Display - High definition (720p) display that is greater than 9” diagonally, 8 bits per color channel.", font=('Areal', 15))
    display_label.grid(row=8, column=0)

    # Buttons
    open_site_button = Button(sq_window, text="Open Site", command=open_site)
    open_site_button.grid(row=9, column=0)

    read_out_button = Button(sq_window, text="Read Out", command=read_out)
    read_out_button.grid(row=10, column=0)

def about_pc_health_check():
    def download_pchc():
        webbrowser.open("https://aka.ms/GetPCHealthCheckApp")

    def read_out():
        try:
            pyttsx3.speak("PC Health Check is a free tool from Microsoft that checks if a computer meets the minimum hardware requirements for Windows 11 and identifies potential issues that could affect the computer's performance with the new operating system.")
        except:
            messagebox.showerror("Error!", "Error: Cannot Read Out!")

    pchc_window = Toplevel()
    pchc_window.title("About PC Health Check")
    pchc_window.resizable(False, False)
    pchc_window.config(padx=25, pady=25)

    # Labels
    pchc_label = Label(pchc_window, text="About PC Health Check", font=('Areal', 25))
    pchc_label.grid(row=0, column=0)

    about_text = "\nPC Health Check is a free tool from Microsoft that checks if a computer meets the minimum hardware requirements for Windows 11.\n It can also identifies potential issues that could affect the computer's performance with the new operating system."
    about_pchc_label = Label(pchc_window, text=about_text)
    about_pchc_label.grid(row=1, column=0)

    placeholder_label = Label(pchc_window, text="")
    placeholder_label.grid(row=2, column=0)

    # Buttons
    download_button = Button(pchc_window, text="Download PC Health Check", width=20, command=download_pchc)
    download_button.grid(row=3, column=0)

    read_out_button = Button(pchc_window, text="Read Out",width=20, command=read_out)
    read_out_button.grid(row=4, column=0)

def how_to_install_win11():
    def open_site():
        webbrowser.open("https://www.microsoft.com/software-download/windows11")

    def read_out():
        try:
            pyttsx3.speak("\nThere are many ways of installing Windows 11 on your Windows 10 PC. The first method is to use the Installation Assistant and it is the easiest. The second method is to download the Media Creation Tool and create a Windows 11 USB Bootable Stick. By using this method, you can clean-install Windows 11 and do many more advanced things. Finally, you can download an ISO file and directly use it or use another software to create a Windows 11 USB Stick. NOTE: Installing Windows 11 on an unsupported PC is very risky. As you will not get important Security Updates! For more info, check out the official website.")
        except:
            messagebox.showerror("Error!", "Error: Cannot Read Out!")

    install_win11_window = Toplevel()
    install_win11_window.title("Install Windows 11")
    install_win11_window.resizable(False, False)
    install_win11_window.config(padx=25, pady=25)

    # Label
    install_win_11_label = Label(install_win11_window, text="Install Windows 11", font=('Areal', 25))
    install_win_11_label.grid(row=0, column=0)

    more_info_label = Label(install_win11_window, text="\nThere are many ways of installing Windows 11 on your Windows 10 PC. \nThe first method is to use the Installation Assistant and it is the easiest.\nThe second method is to download the Media Creation Tool and create a Windows 11 USB Bootable Stick. By using this method, you can clean-install Windows 11 and do many more advanced things. \nFinally, you can download an ISO file and directly use it or use another software to create a Windows 11 USB Stick.")
    more_info_label.grid(row=1, column=0)

    note_label = Label(install_win11_window, text="\nNOTE: Installing Windows 11 on an unsupported PC is very risky. As you will not get important Security Updates!")
    note_label.grid(row=2, column=0)

    more_info_label_2 = Label(install_win11_window, text="For more info, check out the official website.")
    more_info_label_2.grid(row=3, column=0)

    placeholder_label = Label(install_win11_window, text="")
    placeholder_label.grid(row=4, column=0)

    # Buttons
    open_site_button = Button(install_win11_window, text="Open Site", command=open_site)
    open_site_button.grid(row=5, column=0)

    read_out_button = Button(install_win11_window, text="Read Out", command=read_out)
    read_out_button.grid(row=6, column=0)

# GUI Setup
window = Tk()
window.title("Auto11 Installer")
window.resizable(False, False)
window.config(padx=25, pady=25)

# Labels
auto11installer_label = Label(text="Auto11 Installer", font=('Areal', 25))
auto11installer_label.grid(row=0, column=0, sticky='w')

placeholder_label = Label(text="")
placeholder_label.grid(row=1, column=0)

about_win11_label = Label(text="What is Windows 11?")
about_win11_label.grid(row=2, column=0, sticky='w')

system_requirements_label = Label(text="System Requirements for Windows 11")
system_requirements_label.grid(row=3, column=0, sticky='w')

pc_health_check_label = Label(text="What is PC Health Check?")
pc_health_check_label.grid(row=4, column=0, sticky='w')

install_win11_label = Label(text="How to Install Windows 11?")
install_win11_label.grid(row=5, column=0, sticky='w')

# Buttons
about_win11_button = Button(text="About Windows 11", width=15, command=about_win11)
about_win11_button.grid(row=2, column=1)

system_requirements_button = Button(text="System Requirements", width=15, command=system_requirements)
system_requirements_button.grid(row=3, column=1)

about_pchealthcheck_button = Button(text="About PC Health Check", width=15, command=about_pc_health_check)
about_pchealthcheck_button.grid(row=4, column=1)

install_win11_button = Button(text="Install Windows 11", width=15, command=how_to_install_win11)
install_win11_button.grid(row=5, column=1)

window.mainloop()
