import os
import xml.etree.ElementTree as ET

def create_directory():
    if not os.path.exists('assets'):
        os.makedirs('assets')

def create_header_banner():
    svg_content = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 420" width="100%" height="100%">
  <defs>
    <!-- Background Gradients -->
    <linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#080C14"/>
      <stop offset="50%" stop-color="#0F172A"/>
      <stop offset="100%" stop-color="#020617"/>
    </linearGradient>
    
    <linearGradient id="primaryGlow" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#38BDF8"/>
      <stop offset="50%" stop-color="#818CF8"/>
      <stop offset="100%" stop-color="#C084FC"/>
    </linearGradient>

    <linearGradient id="accentGlow" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#34D399"/>
      <stop offset="100%" stop-color="#38BDF8"/>
    </linearGradient>
    
    <linearGradient id="textGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#FFFFFF"/>
      <stop offset="60%" stop-color="#F1F5F9"/>
      <stop offset="100%" stop-color="#94A3B8"/>
    </linearGradient>

    <linearGradient id="titleGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#38BDF8"/>
      <stop offset="40%" stop-color="#A78BFA"/>
      <stop offset="80%" stop-color="#F472B6"/>
    </linearGradient>

    <!-- Radial Light Orbs -->
    <radialGradient id="cyanOrb" cx="20%" cy="30%" r="60%">
      <stop offset="0%" stop-color="#0EA5E9" stop-opacity="0.25"/>
      <stop offset="100%" stop-color="#0EA5E9" stop-opacity="0"/>
    </radialGradient>
    
    <radialGradient id="purpleOrb" cx="80%" cy="70%" r="60%">
      <stop offset="0%" stop-color="#8B5CF6" stop-opacity="0.25"/>
      <stop offset="100%" stop-color="#8B5CF6" stop-opacity="0"/>
    </radialGradient>

    <radialGradient id="emeraldOrb" cx="50%" cy="80%" r="50%">
      <stop offset="0%" stop-color="#10B981" stop-opacity="0.15"/>
      <stop offset="100%" stop-color="#10B981" stop-opacity="0"/>
    </radialGradient>

    <!-- Filters for Glow Effects -->
    <filter id="glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="8" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>
    
    <filter id="subtleGlow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="4" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>

    <!-- Grid Pattern -->
    <pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse">
      <path d="M 40 0 L 0 0 0 40" fill="none" stroke="#334155" stroke-width="1" stroke-opacity="0.15"/>
      <circle cx="40" cy="40" r="1.5" fill="#38BDF8" fill-opacity="0.3"/>
    </pattern>

    <pattern id="dots" width="20" height="20" patternUnits="userSpaceOnUse">
      <circle cx="2" cy="2" r="1" fill="#475569" fill-opacity="0.2"/>
    </pattern>
  </defs>

  <!-- Base Card Container -->
  <rect width="1200" height="420" rx="20" fill="url(#bgGrad)" stroke="#1E293B" stroke-width="2"/>

  <!-- Orbs and Lighting -->
  <rect width="1200" height="420" rx="20" fill="url(#cyanOrb)"/>
  <rect width="1200" height="420" rx="20" fill="url(#purpleOrb)"/>
  <rect width="1200" height="420" rx="20" fill="url(#emeraldOrb)"/>

  <!-- Grid overlay -->
  <rect width="1200" height="420" rx="20" fill="url(#grid)"/>

  <!-- Cyber Neural Connections Graphic (Right Side) -->
  <g transform="translate(740, 40)" opacity="0.85">
    <!-- Network Lines -->
    <path d="M 100 80 L 220 150 L 320 90 L 380 200 L 260 270 L 120 220 Z" fill="none" stroke="#38BDF8" stroke-width="1.5" stroke-dasharray="6,6" opacity="0.4"/>
    <path d="M 220 150 L 260 270" fill="none" stroke="#A78BFA" stroke-width="2" opacity="0.6"/>
    <path d="M 100 80 L 120 220" fill="none" stroke="#34D399" stroke-width="2" opacity="0.5"/>
    <path d="M 320 90 L 380 200" fill="none" stroke="#F472B6" stroke-width="2" opacity="0.5"/>
    
    <!-- Central Node Pulse -->
    <circle cx="220" cy="150" r="45" fill="#818CF8" fill-opacity="0.1" stroke="#818CF8" stroke-width="1" filter="url(#glow)"/>
    <circle cx="220" cy="150" r="25" fill="#38BDF8" fill-opacity="0.2" stroke="#38BDF8" stroke-width="1.5"/>
    <circle cx="220" cy="150" r="8" fill="#38BDF8" filter="url(#subtleGlow)"/>

    <!-- Outer Nodes -->
    <g filter="url(#subtleGlow)">
      <circle cx="100" cy="80" r="6" fill="#38BDF8"/>
      <circle cx="320" cy="90" r="7" fill="#C084FC"/>
      <circle cx="380" cy="200" r="6" fill="#F472B6"/>
      <circle cx="260" cy="270" r="8" fill="#818CF8"/>
      <circle cx="120" cy="220" r="5" fill="#34D399"/>
      <circle cx="180" cy="310" r="4" fill="#38BDF8"/>
    </g>

    <!-- Node Rings -->
    <circle cx="100" cy="80" r="14" fill="none" stroke="#38BDF8" stroke-width="1" stroke-opacity="0.5"/>
    <circle cx="260" cy="270" r="16" fill="none" stroke="#818CF8" stroke-width="1" stroke-opacity="0.5"/>
    <circle cx="320" cy="90" r="15" fill="none" stroke="#C084FC" stroke-width="1" stroke-opacity="0.5"/>

    <!-- Code / Data floating particles -->
    <text x="70" y="55" fill="#38BDF8" font-family="'Fira Code', 'Courier New', monospace" font-size="12" opacity="0.7">&lt;RAG_Engine/&gt;</text>
    <text x="290" y="60" fill="#C084FC" font-family="'Fira Code', 'Courier New', monospace" font-size="12" opacity="0.7">LLM.Orchestrate()</text>
    <text x="310" y="240" fill="#F472B6" font-family="'Fira Code', 'Courier New', monospace" font-size="12" opacity="0.7">Voice_AI.agent()</text>
    <text x="80" y="260" fill="#34D399" font-family="'Fira Code', 'Courier New', monospace" font-size="12" opacity="0.7">OCR.pipeline()</text>
  </g>

  <!-- Left Content Area -->
  <!-- Status Badge -->
  <g transform="translate(60, 50)">
    <rect width="260" height="34" rx="17" fill="#0F172A" stroke="#334155" stroke-width="1"/>
    <rect width="260" height="34" rx="17" fill="url(#titleGrad)" fill-opacity="0.08"/>
    <circle cx="20" cy="17" r="5" fill="#10B981" filter="url(#subtleGlow)"/>
    <text x="35" y="22" fill="#E2E8F0" font-family="'Segoe UI', -apple-system, Roboto, sans-serif" font-size="13" font-weight="600" letter-spacing="0.5">BUILDING PRODUCTION AI</text>
  </g>

  <!-- Main Name Header -->
  <g transform="translate(60, 140)">
    <text x="0" y="0" fill="url(#titleGrad)" font-family="'Segoe UI', -apple-system, BlinkMacSystemFont, 'Montserrat', sans-serif" font-size="52" font-weight="900" letter-spacing="1" filter="url(#subtleGlow)">DHRUV MAVANI</text>
  </g>

  <!-- Professional Subtitle -->
  <g transform="translate(60, 185)">
    <text x="0" y="0" fill="#F1F5F9" font-family="'Segoe UI', -apple-system, Roboto, sans-serif" font-size="22" font-weight="600" letter-spacing="1.5">AI DEVELOPER &amp; LLM SYSTEMS ENGINEER</text>
  </g>

  <!-- Short Tagline -->
  <g transform="translate(60, 220)">
    <text x="0" y="0" fill="#94A3B8" font-family="'Segoe UI', -apple-system, Roboto, sans-serif" font-size="15" font-weight="400">Specializing in Conversational Voice AI, RAG Pipelines, Multi-Agent Workflows &amp; OCR Systems</text>
  </g>

  <!-- Tech Focus Pills -->
  <g transform="translate(60, 260)">
    <!-- Pill 1: RAG & LLMs -->
    <g transform="translate(0, 0)">
      <rect width="155" height="36" rx="10" fill="#1E293B" stroke="#38BDF8" stroke-width="1.2" stroke-opacity="0.5"/>
      <text x="16" y="23" fill="#38BDF8" font-family="'Segoe UI', sans-serif" font-size="13" font-weight="600">⚡ RAG &amp; Vector AI</text>
    </g>
    <!-- Pill 2: Voice Agents -->
    <g transform="translate(167, 0)">
      <rect width="165" height="36" rx="10" fill="#1E293B" stroke="#818CF8" stroke-width="1.2" stroke-opacity="0.5"/>
      <text x="16" y="23" fill="#818CF8" font-family="'Segoe UI', sans-serif" font-size="13" font-weight="600">🎙️ Voice AI (Retell)</text>
    </g>
    <!-- Pill 3: Agents & Orchestration -->
    <g transform="translate(344, 0)">
      <rect width="185" height="36" rx="10" fill="#1E293B" stroke="#C084FC" stroke-width="1.2" stroke-opacity="0.5"/>
      <text x="16" y="23" fill="#C084FC" font-family="'Segoe UI', sans-serif" font-size="13" font-weight="600">🤖 LangChain / Agents</text>
    </g>
    <!-- Pill 4: Vision & OCR -->
    <g transform="translate(541, 0)">
      <rect width="145" height="36" rx="10" fill="#1E293B" stroke="#34D399" stroke-width="1.2" stroke-opacity="0.5"/>
      <text x="16" y="23" fill="#34D399" font-family="'Segoe UI', sans-serif" font-size="13" font-weight="600">🔍 OCR Pipelines</text>
    </g>
  </g>

  <!-- Location & Academic Degree Bar -->
  <g transform="translate(60, 345)">
    <rect width="626" height="40" rx="10" fill="#0F172A" fill-opacity="0.8" stroke="#334155" stroke-width="1"/>
    
    <!-- Education Icon & Text -->
    <text x="20" y="25" fill="#CBD5E1" font-family="'Segoe UI', sans-serif" font-size="13" font-weight="500">🎓 <tspan font-weight="700" fill="#F8FAFC">M.Sc. Artificial Intelligence</tspan> (MKBU) | <tspan font-weight="700" fill="#F8FAFC">BCA Graduate</tspan></text>
    
    <!-- Separator -->
    <line x1="420" y1="10" x2="420" y2="30" stroke="#334155" stroke-width="1.5"/>
    
    <!-- Location -->
    <text x="440" y="25" fill="#CBD5E1" font-family="'Segoe UI', sans-serif" font-size="13" font-weight="500">📍 Gujarat, India</text>
  </g>

  <!-- Top & Bottom Accent Lines -->
  <rect x="0" y="0" width="1200" height="4" rx="2" fill="url(#primaryGlow)"/>
  <rect x="0" y="416" width="1200" height="4" rx="2" fill="url(#titleGrad)"/>
</svg>
'''
    with open('assets/header_banner.svg', 'w', encoding='utf-8') as f:
        f.write(svg_content)
    print("Created assets/header_banner.svg")

def create_skais_banner():
    svg_content = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 320" width="100%" height="100%">
  <defs>
    <linearGradient id="skaisBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0B1329"/>
      <stop offset="50%" stop-color="#0D1B3A"/>
      <stop offset="100%" stop-color="#070D1E"/>
    </linearGradient>
    <linearGradient id="skaisAccent" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#38BDF8"/>
      <stop offset="50%" stop-color="#818CF8"/>
      <stop offset="100%" stop-color="#C084FC"/>
    </linearGradient>
    <filter id="skaisGlow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="6" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>
  </defs>

  <!-- Card Frame -->
  <rect width="1000" height="320" rx="16" fill="url(#skaisBg)" stroke="#1E293B" stroke-width="2"/>
  <rect x="0" y="0" width="1000" height="4" rx="2" fill="url(#skaisAccent)"/>

  <!-- Left Soundwave & AI Agent Visual -->
  <g transform="translate(650, 40)">
    <!-- Voice Soundwave Bars -->
    <rect x="0" y="100" width="8" height="40" rx="4" fill="#38BDF8" opacity="0.6"/>
    <rect x="16" y="70" width="8" height="100" rx="4" fill="#38BDF8" filter="url(#skaisGlow)"/>
    <rect x="32" y="40" width="8" height="160" rx="4" fill="#818CF8" filter="url(#skaisGlow)"/>
    <rect x="48" y="80" width="8" height="80" rx="4" fill="#C084FC"/>
    <rect x="64" y="20" width="8" height="200" rx="4" fill="#38BDF8" filter="url(#skaisGlow)"/>
    <rect x="80" y="60" width="8" height="120" rx="4" fill="#818CF8"/>
    <rect x="96" y="90" width="8" height="60" rx="4" fill="#34D399"/>
    <rect x="112" y="50" width="8" height="140" rx="4" fill="#C084FC" filter="url(#skaisGlow)"/>
    <rect x="128" y="80" width="8" height="80" rx="4" fill="#38BDF8"/>
    <rect x="144" y="110" width="8" height="20" rx="4" fill="#818CF8" opacity="0.5"/>

    <!-- Orbit Rings around soundwave -->
    <circle cx="76" cy="120" r="110" fill="none" stroke="#38BDF8" stroke-width="1" stroke-dasharray="4,8" opacity="0.3"/>
    
    <!-- Floating Tech Metrics Badges -->
    <g transform="translate(-40, 180)">
      <rect width="220" height="44" rx="22" fill="#0F172A" stroke="#38BDF8" stroke-width="1.5"/>
      <text x="20" y="27" fill="#38BDF8" font-family="'Segoe UI', sans-serif" font-size="13" font-weight="700">📞 103+ Production Calls</text>
    </g>
  </g>

  <!-- Main Content Area -->
  <g transform="translate(50, 45)">
    <!-- Badge -->
    <rect width="180" height="28" rx="14" fill="#0F172A" stroke="#38BDF8" stroke-width="1"/>
    <text x="14" y="19" fill="#38BDF8" font-family="'Segoe UI', sans-serif" font-size="12" font-weight="700" letter-spacing="1">FEATURED PROJECT 01</text>

    <!-- Title -->
    <text x="0" y="70" fill="#FFFFFF" font-family="'Segoe UI', sans-serif" font-size="34" font-weight="800">SKAIS — Voice AI Restaurant System</text>

    <!-- Subtitle -->
    <text x="0" y="100" fill="#94A3B8" font-family="'Segoe UI', sans-serif" font-size="15" font-weight="500">Autonomous Conversational AI Order &amp; Reservation Platform</text>

    <!-- Highlights Bullet List -->
    <g transform="translate(0, 130)">
      <text x="0" y="0" fill="#E2E8F0" font-family="'Segoe UI', sans-serif" font-size="14">🔹 <tspan font-weight="700" fill="#F8FAFC">Retell AI Voice Agent</tspan> taking live customer phone orders &amp; reservations autonomously</text>
      <text x="0" y="28" fill="#E2E8F0" font-family="'Segoe UI', sans-serif" font-size="14">🔹 <tspan font-weight="700" fill="#F8FAFC">RAG Knowledge Base</tspan> answering restaurant hours, policies, &amp; menu items accurately</text>
      <text x="0" y="56" fill="#E2E8F0" font-family="'Segoe UI', sans-serif" font-size="14">🔹 <tspan font-weight="700" fill="#F8FAFC">FastAPI + Supabase + Twilio SDK</tspan> for instant SMS order confirmations &amp; prep-time logic</text>
      <text x="0" y="84" fill="#E2E8F0" font-family="'Segoe UI', sans-serif" font-size="14">🔹 <tspan font-weight="700" fill="#F8FAFC">50%+ Cost Reduction</tspan> ($1,000–$1,500/mo software cost vs $2,000–$3,000/mo human operator)</text>
    </g>
  </g>

  <!-- Stack Pills Row -->
  <g transform="translate(50, 272)">
    <text x="0" y="16" fill="#64748B" font-family="'Segoe UI', sans-serif" font-size="12" font-weight="700" letter-spacing="1">TECH STACK:</text>
    
    <g transform="translate(85, 0)">
      <rect width="70" height="24" rx="6" fill="#1E293B"/><text x="10" y="16" fill="#38BDF8" font-family="sans-serif" font-size="11" font-weight="600">Python</text>
    </g>
    <g transform="translate(163, 0)">
      <rect width="70" height="24" rx="6" fill="#1E293B"/><text x="10" y="16" fill="#818CF8" font-family="sans-serif" font-size="11" font-weight="600">FastAPI</text>
    </g>
    <g transform="translate(241, 0)">
      <rect width="95" height="24" rx="6" fill="#1E293B"/><text x="10" y="16" fill="#C084FC" font-family="sans-serif" font-size="11" font-weight="600">Retell AI SDK</text>
    </g>
    <g transform="translate(344, 0)">
      <rect width="70" height="24" rx="6" fill="#1E293B"/><text x="10" y="16" fill="#34D399" font-family="sans-serif" font-size="11" font-weight="600">LangChain</text>
    </g>
    <g transform="translate(422, 0)">
      <rect width="75" height="24" rx="6" fill="#1E293B"/><text x="10" y="16" fill="#F472B6" font-family="sans-serif" font-size="11" font-weight="600">Supabase</text>
    </g>
    <g transform="translate(505, 0)">
      <rect width="70" height="24" rx="6" fill="#1E293B"/><text x="10" y="16" fill="#FBBF24" font-family="sans-serif" font-size="11" font-weight="600">Twilio SDK</text>
    </g>
    <g transform="translate(583, 0)">
      <rect width="65" height="24" rx="6" fill="#1E293B"/><text x="10" y="16" fill="#60A5FA" font-family="sans-serif" font-size="11" font-weight="600">Next.js</text>
    </g>
  </g>
</svg>
'''
    with open('assets/skais_banner.svg', 'w', encoding='utf-8') as f:
        f.write(svg_content)
    print("Created assets/skais_banner.svg")

def create_exambro_banner():
    svg_content = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 320" width="100%" height="100%">
  <defs>
    <linearGradient id="exambroBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#140B29"/>
      <stop offset="50%" stop-color="#1C1138"/>
      <stop offset="100%" stop-color="#090518"/>
    </linearGradient>
    <linearGradient id="exambroAccent" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#A78BFA"/>
      <stop offset="50%" stop-color="#F472B6"/>
      <stop offset="100%" stop-color="#34D399"/>
    </linearGradient>
    <filter id="exambroGlow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="6" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>
  </defs>

  <!-- Card Frame -->
  <rect width="1000" height="320" rx="16" fill="url(#exambroBg)" stroke="#1E293B" stroke-width="2"/>
  <rect x="0" y="0" width="1000" height="4" rx="2" fill="url(#exambroAccent)"/>

  <!-- Right Visual Graphics: PDF OCR Scanner Simulation -->
  <g transform="translate(680, 45)">
    <!-- PDF Document Outline -->
    <rect width="160" height="210" rx="10" fill="#0F172A" stroke="#A78BFA" stroke-width="2"/>
    <line x1="25" y1="35" x2="135" y2="35" stroke="#E2E8F0" stroke-width="3" stroke-linecap="round"/>
    <line x1="25" y1="55" x2="115" y2="55" stroke="#94A3B8" stroke-width="2" stroke-linecap="round"/>
    <line x1="25" y1="70" x2="100" y2="70" stroke="#94A3B8" stroke-width="2" stroke-linecap="round"/>
    
    <!-- Diagram Box inside document -->
    <rect x="25" y="90" width="110" height="60" rx="6" fill="#1E293B" stroke="#34D399" stroke-width="1.5" stroke-dasharray="3,3"/>
    <polygon points="40,135 65,105 90,135" fill="none" stroke="#34D399" stroke-width="2"/>
    <circle cx="105" cy="110" r="8" fill="#F472B6"/>

    <!-- OCR Scanning Beam Line -->
    <line x1="10" y1="120" x2="170" y2="120" stroke="#F472B6" stroke-width="3" filter="url(#exambroGlow)"/>

    <line x1="25" y1="165" x2="135" y2="165" stroke="#94A3B8" stroke-width="2" stroke-linecap="round"/>
    <line x1="25" y1="180" x2="85" y2="180" stroke="#94A3B8" stroke-width="2" stroke-linecap="round"/>

    <!-- Gemini AI Sparkle Icon -->
    <g transform="translate(130, -10)" filter="url(#exambroGlow)">
      <circle cx="20" cy="20" r="22" fill="#8B5CF6"/>
      <path d="M 20 8 L 23 17 L 32 20 L 23 23 L 20 32 L 17 23 L 8 20 L 17 17 Z" fill="#FFFFFF"/>
    </g>
  </g>

  <!-- Left Content Area -->
  <g transform="translate(50, 45)">
    <!-- Badge -->
    <rect width="180" height="28" rx="14" fill="#0F172A" stroke="#A78BFA" stroke-width="1"/>
    <text x="14" y="19" fill="#A78BFA" font-family="'Segoe UI', sans-serif" font-size="12" font-weight="700" letter-spacing="1">FEATURED PROJECT 02</text>

    <!-- Title -->
    <text x="0" y="70" fill="#FFFFFF" font-family="'Segoe UI', sans-serif" font-size="34" font-weight="800">ExamBro — OCR &amp; Exam Extraction</text>

    <!-- Subtitle -->
    <text x="0" y="100" fill="#94A3B8" font-family="'Segoe UI', sans-serif" font-size="15" font-weight="500">Automated Question, Diagram &amp; Solution Extraction Pipeline</text>

    <!-- Highlights Bullet List -->
    <g transform="translate(0, 130)">
      <text x="0" y="0" fill="#E2E8F0" font-family="'Segoe UI', sans-serif" font-size="14">🔹 <tspan font-weight="700" fill="#F8FAFC">Mistral OCR + PyMuPDF</tspan> pipeline pulling questions, options &amp; diagrams straight from PDFs</text>
      <text x="0" y="28" fill="#E2E8F0" font-family="'Segoe UI', sans-serif" font-size="14">🔹 <tspan font-weight="700" fill="#F8FAFC">Diagram Alignment Engine</tspan> resolving recurring spatial displacement bugs in OCR output</text>
      <text x="0" y="56" fill="#E2E8F0" font-family="'Segoe UI', sans-serif" font-size="14">🔹 <tspan font-weight="700" fill="#F8FAFC">Gemini AI via LangChain</tspan> converting raw text into structured JSON &amp; auto-filling answers</text>
      <text x="0" y="84" fill="#E2E8F0" font-family="'Segoe UI', sans-serif" font-size="14">🔹 <tspan font-weight="700" fill="#F8FAFC">Docker Containerized</tspan> with multilingual translation &amp; bulk admin dashboard</text>
    </g>
  </g>

  <!-- Stack Pills Row -->
  <g transform="translate(50, 272)">
    <text x="0" y="16" fill="#64748B" font-family="'Segoe UI', sans-serif" font-size="12" font-weight="700" letter-spacing="1">TECH STACK:</text>
    
    <g transform="translate(85, 0)">
      <rect width="70" height="24" rx="6" fill="#1E293B"/><text x="10" y="16" fill="#A78BFA" font-family="sans-serif" font-size="11" font-weight="600">Python</text>
    </g>
    <g transform="translate(163, 0)">
      <rect width="70" height="24" rx="6" fill="#1E293B"/><text x="10" y="16" fill="#F472B6" font-family="sans-serif" font-size="11" font-weight="600">Django</text>
    </g>
    <g transform="translate(241, 0)">
      <rect width="70" height="24" rx="6" fill="#1E293B"/><text x="10" y="16" fill="#38BDF8" font-family="sans-serif" font-size="11" font-weight="600">FastAPI</text>
    </g>
    <g transform="translate(319, 0)">
      <rect width="85" height="24" rx="6" fill="#1E293B"/><text x="10" y="16" fill="#34D399" font-family="sans-serif" font-size="11" font-weight="600">Mistral OCR</text>
    </g>
    <g transform="translate(412, 0)">
      <rect width="85" height="24" rx="6" fill="#1E293B"/><text x="10" y="16" fill="#FBBF24" font-family="sans-serif" font-size="11" font-weight="600">Gemini AI</text>
    </g>
    <g transform="translate(505, 0)">
      <rect width="75" height="24" rx="6" fill="#1E293B"/><text x="10" y="16" fill="#818CF8" font-family="sans-serif" font-size="11" font-weight="600">PyMuPDF</text>
    </g>
    <g transform="translate(588, 0)">
      <rect width="65" height="24" rx="6" fill="#1E293B"/><text x="10" y="16" fill="#60A5FA" font-family="sans-serif" font-size="11" font-weight="600">Docker</text>
    </g>
  </g>
</svg>
'''
    with open('assets/exambro_banner.svg', 'w', encoding='utf-8') as f:
        f.write(svg_content)
    print("Created assets/exambro_banner.svg")

def create_quote_card():
    svg_content = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 160" width="100%" height="100%">
  <defs>
    <linearGradient id="quoteBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0F172A"/>
      <stop offset="50%" stop-color="#1E1B4B"/>
      <stop offset="100%" stop-color="#090D16"/>
    </linearGradient>
    <linearGradient id="quoteTextGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#38BDF8"/>
      <stop offset="50%" stop-color="#A78BFA"/>
      <stop offset="100%" stop-color="#F472B6"/>
    </linearGradient>
    <filter id="quoteGlow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="4" result="blur"/>
      <feComposite in="SourceGraphic" in2="blur" operator="over"/>
    </filter>
  </defs>

  <rect width="1000" height="160" rx="16" fill="url(#quoteBg)" stroke="#334155" stroke-width="1.5"/>
  <rect x="0" y="0" width="6" height="160" rx="3" fill="url(#quoteTextGrad)"/>

  <g transform="translate(45, 45)">
    <!-- Large Quote Mark Graphic -->
    <text x="0" y="45" fill="#38BDF8" font-family="'Georgia', serif" font-size="70" opacity="0.25">“</text>
    
    <!-- Quote Body -->
    <text x="45" y="32" fill="#F8FAFC" font-family="'Segoe UI', -apple-system, sans-serif" font-size="20" font-weight="600" font-style="italic" letter-spacing="0.3">
      "Ever tried. Ever failed. No matter. Try again. Fail again. Fail better"
    </text>
    
    <!-- Author Attribution -->
    <g transform="translate(45, 68)">
      <rect width="160" height="26" rx="13" fill="#1E293B" stroke="#818CF8" stroke-width="1"/>
      <text x="16" y="18" fill="url(#quoteTextGrad)" font-family="'Segoe UI', sans-serif" font-size="13" font-weight="700" filter="url(#quoteGlow)">— Samuel Beckett</text>
    </g>
  </g>
</svg>
'''
    with open('assets/quote_card.svg', 'w', encoding='utf-8') as f:
        f.write(svg_content)
    print("Created assets/quote_card.svg")

def create_divider():
    svg_content = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 24" width="100%" height="100%">
  <defs>
    <linearGradient id="divGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#38BDF8" stop-opacity="0"/>
      <stop offset="25%" stop-color="#38BDF8"/>
      <stop offset="50%" stop-color="#A78BFA"/>
      <stop offset="75%" stop-color="#F472B6"/>
      <stop offset="100%" stop-color="#F472B6" stop-opacity="0"/>
    </linearGradient>
  </defs>
  <rect x="50" y="11" width="900" height="2" rx="1" fill="url(#divGrad)"/>
  <circle cx="500" cy="12" r="5" fill="#A78BFA"/>
  <circle cx="500" cy="12" r="2" fill="#FFFFFF"/>
</svg>
'''
    with open('assets/divider.svg', 'w', encoding='utf-8') as f:
        f.write(svg_content)
    print("Created assets/divider.svg")

if __name__ == '__main__':
    create_directory()
    create_header_banner()
    create_skais_banner()
    create_exambro_banner()
    create_quote_card()
    create_divider()
