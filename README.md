# 🗳️ ELECAM GAROUA VOTE IA

**Application de vote en ligne ULTRA PREMIUM** - Système de voting sécurisé avec vérification faciale IA, anti-fraude intelligente et bureau administratif.

## 🌟 Caractéristiques Principales

### 🎨 Design Premium
- **UI Glassmorphism** avec Tailwind CSS + Framer Motion
- **Couleurs Cameroun**: Vert (#006400), Jaune (#FFD700), Rouge (#CE1126)
- **100% Responsive** - Mobile first, animations fluides
- **Typo Elite**: Inter + Poppins Bold

### 🤖 IA & Sécurité
- **OCR Carte Électorale**: Tesseract.js pour lecture automatique CNI
- **Vérification Faciale**: DeepFace ArcFace avec seuil 0.40, confiance >75%
- **Anti-Fraude Automatique**: Blocage instantané des doublons CNI/Visage/Device
- **Face Matching en Temps Réel**: Cercle de confiance animé 0-100%

### 🏛️ Flux Complet
1. **Splash Screen Premium** - Logo ELECAM avec animation pulse + progress bar
2. **KYC IA** - Upload carte électorale + OCR automatique
3. **Selfie Faciale** - Capture live avec cadre oval (style Face ID)
4. **Scrutins Multiples** - Présidentielle, Législatives, Municipales
5. **Confirmation QR** - Preuve de vote avec signature numérique
6. **Bureau Admin** - Dashboard temps réel + Export PDF/Excel

---

## 🛠️ Stack Technique

### Frontend
```
React 18 + Vite
Tailwind CSS + Framer Motion
face-api.js (Face Detection)
Tesseract.js (OCR)
axios (API calls)
```

### Backend
```
FastAPI + Uvicorn
SQLite (Database)
DeepFace (Face Recognition)
OpenCV (Image Processing)
qrcode + reportlab (PDF/QR)
openpyxl (Excel Export)
```

---

## 📦 Installation

### Prérequis
- Node.js 18+
- Python 3.9+
- Caméra frontale et microphone

### Frontend Setup
```bash
cd frontend
npm install
npm run dev
```

### Backend Setup
```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
python main.py
```

Backend sera disponible sur: **http://localhost:8000**
Frontend sera disponible sur: **http://localhost:5173**

---

## 🔐 Authentification Admin

**Code d'accès**: `GAROUA2025`

Dashboard administratif accessible après login.

---

## 📋 Structure du Projet

```
elecam-garoua-vote-ia/
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── SplashScreen.jsx
│   │   │   ├── KYC/
│   │   │   │   ├── CardUpload.jsx
│   │   │   │   └── CardOCR.jsx
│   │   │   ├── FacialVerification/
│   │   │   │   ├── SelfieCapture.jsx
│   │   │   │   └── FaceComparison.jsx
│   │   │   ├── Voting/
│   │   │   │   ├── ElectionsTab.jsx
│   │   │   │   └── CandidateCard.jsx
│   │   │   ├── Confirmation/
│   │   │   │   └── QRCode.jsx
│   │   │   └── Admin/
│   │   │       ├── Dashboard.jsx
│   │   │       ├── FraudList.jsx
│   │   │       └── ResultsChart.jsx
│   │   ├── styles/
│   │   │   └── tailwind.css
│   │   ├── App.jsx
│   │   └── main.jsx
│   ├── package.json
│   └── vite.config.js
│
├── backend/
│   ├── main.py
│   ├── models/
│   │   ├── voter.py
│   │   ├── fraud.py
│   │   └── election.py
│   ├── routes/
│   │   ├── kyc.py
│   │   ├── facial.py
│   │   ├── voting.py
│   │   ├── admin.py
│   │   └── fraud.py
│   ├── services/
│   │   ├── ocr_service.py
│   │   ├── face_recognition.py
│   │   └── fraud_detection.py
│   ├── db.py
│   ├── requirements.txt
│   └── config.py
│
└── README.md
```

---

## 🚀 Démarrage Rapide

### 1. Clone et Setup
```bash
git clone https://github.com/godlovesegning8-rgb/elecam-garoua-vote-ia.git
cd elecam-garoua-vote-ia
```

### 2. Backend
```bash
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python main.py
```

### 3. Frontend (Nouvel onglet terminal)
```bash
cd frontend
npm install
npm run dev
```

### 4. Accès
- **App Votant**: http://localhost:5173
- **API Backend**: http://localhost:8000
- **Admin**: http://localhost:5173/admin (Code: GAROUA2025)

---

## 🎯 Flux Votant Complet

### Phase 1: Splash & Home
- Animation logo 2.5s avec progress bar verte
- Stats temps réel: total votants, taux participation
- Bouton "Commencer Vote"

### Phase 2: KYC IA
- Upload photo carte électorale
- OCR détecte automatiquement numéro CNI + nom
- Extraction automatique du visage
- Permet correction manuelle si besoin

### Phase 3: Vérification Faciale
- Capture selfie live (cadre oval Face ID style)
- Comparaison DeepFace ArcFace en temps réel
- Affichage cercle de confiance 0-100%
- **VERIFIE** ✅ ou **ECHEC** ❌

### Phase 4: Vote
- 3 onglets scrutins (Présidentielle, Législatives, Municipales)
- Cartes candidats avec photo ronde, parti, programme
- Animations hover 3D

### Phase 5: Confirmation & QR
- Animation succès
- QR code officiel avec infos vote
- Signature numérique
- Téléchargement preuve PDF

---

## 🛡️ Anti-Fraude Automatique

**Système bloque instantanément si:**
- ❌ Même CNI déjà voté pour même scrutin
- ❌ Même VISAGE (face_hash) même avec CNI différent → "Fraude faciale détectée"
- ❌ Même Device ID déjà voté

**Chaque tentative frauduleuse enregistrée** avec:
- Photo du visage
- Raison fraude
- Date + Heure
- CNI tentée

---

## 📊 Bureau Administratif

### Login
Code d'accès: **GAROUA2025**

### Fonctionnalités
✅ **Dashboard Temps Réel**
- Graphiques Chart.js par scrutin
- Statistiques participation
- Résultats en direct

✅ **Gestion Bureau**
- Ouvrir/Fermer vote (bloque tout si fermé)
- Liste votants (CNI, nom, confiance faciale, date)
- Liste fraudeurs avec photos et raisons

✅ **Résultats & Export**
- Résultats par candidat avec % et barres animées
- Export Excel complet
- PV PDF officiel (logo ELECAM, cachet, signature)

❌ **Validation Manuelle DESACTIVEE**
- Système IA automatique SEULEMENT
- Aucun administrateur ne peut valider manuellement

---

## 🔧 Configuration

### Backend (config.py)
```python
FACE_CONFIDENCE_THRESHOLD = 0.40
FACE_RECOGNITION_THRESHOLD = 75
MAX_FACE_DISTANCE = 0.40
OCR_CONFIDENCE_MIN = 0.80
ADMIN_CODE = "GAROUA2025"
CAMEROON_GREEN = "#006400"
CAMEROON_YELLOW = "#FFD700"
CAMEROON_RED = "#CE1126"
```

---

## 📱 Responsivité

- ✅ **Mobile**: 320px - 767px
- ✅ **Tablet**: 768px - 1023px
- ✅ **Desktop**: 1024px+
- ✅ **Animations fluides** sur tous les devices

---

## 📄 Licence

MIT License - Libre d'utilisation

---

## 👨‍💻 Développeur

**ELECAM GAROUA VOTE IA** - Made with ❤️ for Cameroon

---

## 📞 Support

Pour les issues ou questions: GitHub Issues

---

**Bienvenue dans l'avenir du vote sécurisé! 🇨🇲🗳️✨**