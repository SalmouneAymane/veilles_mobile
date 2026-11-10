---
marp: true
theme: default
paginate: true
style: |
  @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');
  
  section {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    background: linear-gradient(135deg, #1e3a8a 0%, #3b82f6 100%);
    color: white;
    padding: 50px 70px;
    font-size: 1.2em;
  }
  
  section.title {
    background: linear-gradient(135deg, #0f172a 0%, #1e40af 100%);
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
  }
  
  section.content {
    background: white;
    color: #1e293b;
  }
  
  h1 {
    font-size: 2.5em;
    font-weight: 700;
    margin-bottom: 0.3em;
    color: #60a5fa;
    text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
  }
  
  h2 {
    font-size: 1.6em;
    font-weight: 600;
    color: #60a5fa;
    margin-bottom: 0.6em;
    margin-top: 0.3em;
    border-bottom: 3px solid #60a5fa;
    padding-bottom: 0.2em;
  }
  
  h3 {
    font-size: 1.3em;
    font-weight: 600;
    color: #93c5fd;
    margin: 0.8em 0 0.4em 0;
  }
  
  section.content h2 {
    color: #3b82f6;
    border-bottom-color: #3b82f6;
  }
  
  section.content h3 {
    color: #1e40af;
  }
  
  ul {
    font-size: 1em;
    line-height: 1.6;
    margin: 0.5em 0;
  }
  
  li {
    margin: 0.4em 0;
  }
  
  strong {
    color: #93c5fd;
    font-weight: 600;
  }
  
  section.content strong {
    color: #3b82f6;
  }
  
  blockquote {
    border-left: 5px solid #60a5fa;
    padding: 12px 20px;
    font-style: italic;
    font-size: 1.1em;
    background: rgba(255,255,255,0.1);
    border-radius: 8px;
    margin: 1em 0;
  }
  
  section.content blockquote {
    border-left-color: #3b82f6;
    background: #eff6ff;
    color: #1e40af;
  }
  
  table {
    width: 100%;
    border-collapse: collapse;
    margin: 1em 0;
    font-size: 0.9em;
  }
  
  section.content table {
    border: 2px solid #e2e8f0;
  }
  
  th {
    background: rgba(0,0,0,0.3);
    padding: 12px;
    font-weight: 600;
  }
  
  section.content th {
    background: #3b82f6;
    color: white;
  }
  
  td {
    padding: 10px 12px;
    border-bottom: 1px solid rgba(255,255,255,0.2);
  }
  
  section.content td {
    border-bottom-color: #e2e8f0;
  }
  
  code {
    background: rgba(0,0,0,0.3);
    padding: 2px 6px;
    border-radius: 4px;
    font-family: 'Fira Code', monospace;
    font-size: 0.85em;
  }
  
  section.content code {
    background: #f1f5f9;
    color: #be123c;
  }
  
  pre {
    background: rgba(0,0,0,0.4);
    padding: 15px;
    border-radius: 8px;
    overflow-x: auto;
    margin: 0.8em 0;
    font-size: 0.75em;
  }
  
  section.content pre {
    background: #1e293b;
  }
  
  pre code {
    background: transparent;
    color: #e2e8f0;
  }
  
  footer {
    font-size: 0.7em;
  }
---

<!-- _class: title -->
<!-- _paginate: false -->

# 🤖 OpenCode.ai

### Assistant de Code IA pour le Développement Moderne

**Mohammed Yassir MESBAHI**
ES-SARRAJ Fouad | OFPPT Solicode | Nov 2026

---

<!-- _class: content -->

## 📋 Qu'est-ce qu'OpenCode.ai ?

Assistant de développement alimenté par l'IA qui accélère le codage

**Caractéristiques**
- 🤖 Assistant IA intelligent
- 💻 Support multi-langages (Python, JS, Java, C++, Go...)
- 🚀 Productivité x2-3
- 🔌 Intégration IDE (VS Code, JetBrains, Vim)

---

<!-- _class: content -->

## ✨ Fonctionnalités Principales

| Fonction | Description |
|:---|:---|
| **Génération** | Fonctions complètes depuis descriptions naturelles |
| **Complétion** | Suggestions contextuelles multi-lignes |
| **Refactoring** | Optimisation et amélioration automatiques |
| **Documentation** | Génération auto de docs et commentaires |
| **Tests** | Création de tests unitaires |

---

<!-- _class: content -->

## 🔄 Architecture

```
┌─────────────────────────┐
│       Votre IDE         │
├─────────────────────────┤
│  Extension OpenCode.ai  │
├─────────────────────────┤
│   Moteur IA (Cloud)     │
├─────────────────────────┤
│ Suggestions Instantanées│
└─────────────────────────┘
```

---

<!-- _class: content -->

## 👨‍💻 Exemple : Validation Email

**Prompt:** *"Fonction validation email"*

```python
import re

def validate_email(email: str) -> bool:
    """Valide une adresse email."""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None
```

✨ Généré en 2 secondes avec documentation !

---

<!-- _class: content -->

## 💼 Cas d'Usage

**Pour Développeurs**
- ⚡ Code 2-3x plus rapide
- 📚 Apprentissage de nouveaux langages
- 🐛 Détection précoce de bugs

**Pour Équipes**
- 🤝 Style de code cohérent
- 📖 Onboarding rapide
- 🔍 Revues automatisées

---

<!-- _class: content -->

## 🚀 Démarrage Rapide

**Installation**
```bash
code --install-extension opencode-ai
```

**Configuration**
1. Inscription sur opencode.ai
2. Récupération clé API
3. Configuration IDE

**Utilisation**
- Tapez → Suggestions apparaissent
- Raccourcis pour génération complète

---

<!-- _class: content -->

## 💰 Tarification

**Gratuit**
- Complétions de base
- Requêtes limitées
- 🎓 Parfait pour étudiants

**Pro - 15$/mois**
- ✅ Illimité
- ✅ Modèles avancés
- ✅ Support prioritaire
- ✅ Collaboration équipe

---

<!-- _class: content -->

## 🔒 Sécurité & Confidentialité

**Protection**
- 🔒 Chiffrement bout-en-bout
- 🛡️ Pas d'entraînement sur votre code
- 📋 RGPD compliant
- 🏢 Déploiement sur site disponible

**Contrôle total**
- Configuration des données partagées
- Options de désactivation
- Transparence complète

---

<!-- _class: content -->

## 📊 Comparaison Concurrents

| Feature | OpenCode | Copilot | Tabnine |
|:---|:---:|:---:|:---:|
| Gratuit | ✅ | ❌ | ✅ |
| Local | ✅ | ❌ | ✅ |
| Privacy | ✅ | ⚠️ | ✅ |
| Prix/mois | 15$ | 10$ | 12$ |

---

<!-- _class: content -->

## 💬 Témoignages

> "Temps de dev réduit de 40%. Comme avoir un senior toujours disponible."
> — **Sarah M., Full-Stack**

> "Invaluable pour nos juniors. Courbe d'apprentissage accélérée."
> — **Ahmed K., Lead**

---

<!-- _class: content -->

## 🇲🇦 Contexte Marocain

**Opportunités**
- 🌍 Tech marocaine en croissance
- 💼 Travail à distance facilité
- 🎓 Apprentissage accéléré
- 🚀 MVP rapides pour startups

**Communauté**
- Meetups tech locaux
- Partage d'expériences
- Collaboration

---

<!-- _class: content -->

## 🔄 Alternatives

| Outil | Avantage |
|:---|:---|
| **GitHub Copilot** | Intégration GitHub |
| **Tabnine** | Modèles locaux |
| **Codeium** | Gratuit illimité |
| **Cursor** | Éditeur IA-first |

---

<!-- _class: content -->

## ⚠️ Points de Vigilance

**Ne pas oublier**
- 📚 Continuer à apprendre les bases
- 🔍 Toujours vérifier le code généré
- 🔐 Attention aux vulnérabilités
- ⚖️ Comprendre avant d'implémenter

**L'IA assiste, ne remplace pas**

---

<!-- _class: content -->

## 🎯 Vision Future

**Tendances 2027**
- 🎨 IA multimodale (design → code)
- 🎤 Voix vers code
- 🔍 Débogage prédictif
- 👥 Collaboration IA-équipe

**Impact**
- Démocratisation du code
- Focus sur créativité
- Innovation accélérée

---

<!-- _class: content -->

## 🎓 Compétences Acquises

**Techniques**
- Compréhension outils IA de dev
- Analyse comparative marché
- Identification use cases

**Transversales**
- Veille technologique
- Synthèse d'information
- Évaluation critique

---

<!-- _class: title -->
<!-- _paginate: false -->

# 🙏 Merci !

**Adoptez le Développement Assisté par IA**

[opencode.ai](https://opencode.ai)

*"Le meilleur code est celui qu'on n'écrit pas soi-même"*

---

<!-- _class: title -->
<!-- _paginate: false -->

# ❓ Questions ?

**Mohammed Yassir MESBAHI**
📧 mesbahi@solicode.ma

**ES-SARRAJ Fouad**
🏢 OFPPT Solicode

**OFPPT Solicode © 2026**
