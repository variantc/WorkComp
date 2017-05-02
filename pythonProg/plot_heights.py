from numpy import zeros
import matplotlib.pyplot as plt

h = zeros(4)
h[0] = 1.6; h[1] = 1.85; h [2] = 1.75; h[3] = 1.80
H = zeros(4)
H[0] = 0.5; H[1] = 0.70; H [2] = 1.90; H[3] = 1.80

familyMemberNo = zeros(4)
familyMemberNo[0] = 0; familyMemberNo[1] = 1;
familyMemberNo[2] = 2; familyMemberNo[3] = 3;

plt.plot(familyMemberNo, h) 
plt.plot(familyMemberNo, H, '-')
plt.xlabel("Family member number")
plt.ylabel("Height (m)")
plt.title("Figure 1 - Heights")
plt.legend("hH")
plt.show()
