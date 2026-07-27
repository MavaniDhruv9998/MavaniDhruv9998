import os

def create_hero_banner():
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 850 250" width="100%" height="100%">
  <defs>
    <linearGradient id="bg-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0B0F19" />
      <stop offset="50%" stop-color="#111827" />
      <stop offset="100%" stop-color="#070A11" />
    </linearGradient>
    <linearGradient id="border-grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#00F2FE" />
      <stop offset="50%" stop-color="#9D4EDD" />
      <stop offset="100%" stop-color="#F43F5E" />
    </linearGradient>
    <linearGradient id="text-grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#00F2FE" />
      <stop offset="40%" stop-color="#4FACFE" />
      <stop offset="80%" stop-color="#00C6FF" />
      <stop offset="100%" stop-color="#A855F7" />
    </linearGradient>
    <linearGradient id="badge-grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="rgba(0, 242, 254, 0.18)" />
      <stop offset="100%" stop-color="rgba(157, 78, 221, 0.18)" />
    </linearGradient>
    <filter id="glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="6" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>
    <filter id="subtle-glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="3" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>
    <pattern id="grid" width="30" height="30" patternUnits="userSpaceOnUse">
      <path d="M 30 0 L 0 0 0 30" fill="none" stroke="rgba(255, 255, 255, 0.03)" stroke-width="1"/>
      <circle cx="30" cy="30" r="1" fill="rgba(0, 242, 254, 0.15)"/>
    </pattern>
    <style>
      .title { font-family: 'Inter', 'Segoe UI', system-ui, -apple-system, sans-serif; font-weight: 900; font-size: 40px; fill: url(#text-grad); letter-spacing: 1.5px; }
      .badge-text { font-family: 'Fira Code', 'Segoe UI', monospace; font-size: 13px; font-weight: 700; fill: #00F2FE; letter-spacing: 1px; }
      .subtitle { font-family: 'Inter', 'Segoe UI', sans-serif; font-weight: 500; font-size: 16px; fill: #94A3B8; letter-spacing: 0.5px; }
      .chip-text { font-family: 'Inter', 'Segoe UI', sans-serif; font-size: 13px; font-weight: 600; fill: #E2E8F0; }
      .status-text { font-family: 'Inter', 'Segoe UI', sans-serif; font-size: 12px; font-weight: 600; fill: #10B981; }
      @keyframes pulseDot {
        0% { r: 4px; opacity: 1; }
        50% { r: 7px; opacity: 0.4; }
        100% { r: 4px; opacity: 1; }
      }
      .animated-dot { animation: pulseDot 2s infinite ease-in-out; fill: #10B981; }
    </style>
  </defs>

  <rect x="2" y="2" width="846" height="246" rx="16" fill="url(#bg-grad)" stroke="url(#border-grad)" stroke-width="2" />
  <rect x="2" y="2" width="846" height="246" rx="16" fill="url(#grid)" />

  <circle cx="100" cy="50" r="80" fill="#00F2FE" opacity="0.06" filter="url(#glow)" />
  <circle cx="750" cy="200" r="100" fill="#9D4EDD" opacity="0.08" filter="url(#glow)" />

  <g transform="translate(40, 28)">
    <rect x="0" y="0" width="280" height="28" rx="14" fill="url(#badge-grad)" stroke="#00F2FE" stroke-opacity="0.4" stroke-width="1" />
    <text x="14" y="19" class="badge-text">🤖 AI DEVELOPER &amp; LLM ARCHITECT</text>
  </g>

  <text x="40" y="96" class="title" filter="url(#subtle-glow)">DHRUV MAVANI</text>
  <text x="40" y="126" class="subtitle">Specializing in Voice AI Agents, RAG Pipelines &amp; Production Enterprise AI</text>

  <g transform="translate(40, 148)">
    <g transform="translate(0, 0)">
      <rect x="0" y="0" width="210" height="34" rx="8" fill="rgba(255, 255, 255, 0.04)" stroke="rgba(255, 255, 255, 0.1)" stroke-width="1"/>
      <text x="14" y="22" class="chip-text">⚡ 7+ Months AI Experience</text>
    </g>
    <g transform="translate(222, 0)">
      <rect x="0" y="0" width="215" height="34" rx="8" fill="rgba(255, 255, 255, 0.04)" stroke="rgba(255, 255, 255, 0.1)" stroke-width="1"/>
      <text x="14" y="22" class="chip-text">🚀 2 Production Platforms</text>
    </g>
    <g transform="translate(449, 0)">
      <rect x="0" y="0" width="210" height="34" rx="8" fill="rgba(255, 255, 255, 0.04)" stroke="rgba(255, 255, 255, 0.1)" stroke-width="1"/>
      <text x="14" y="22" class="chip-text">🎓 M.Sc. Artificial Intelligence</text>
    </g>
  </g>

  <g transform="translate(40, 200)">
    <rect x="0" y="0" width="460" height="26" rx="13" fill="rgba(16, 185, 129, 0.1)" stroke="rgba(16, 185, 129, 0.3)" stroke-width="1"/>
    <circle cx="16" cy="13" r="4" class="animated-dot" />
    <text x="28" y="17" class="status-text">AVAILABLE FOR FULL-TIME ROLES &amp; SYSTEM ARCHITECTURE</text>
  </g>
</svg>'''
    with open('assets/hero_banner.svg', 'w', encoding='utf-8') as f:
        f.write(svg)
    print("Created hero_banner.svg")

def create_ai_metrics():
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 850 165" width="100%" height="100%">
  <defs>
    <linearGradient id="bg-grad-m" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0F172A" />
      <stop offset="100%" stop-color="#0B0F19" />
    </linearGradient>
    <linearGradient id="card-grad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="rgba(30, 41, 59, 0.7)" />
      <stop offset="100%" stop-color="rgba(15, 23, 42, 0.7)" />
    </linearGradient>
    <linearGradient id="cyan-glow" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#00F2FE" />
      <stop offset="100%" stop-color="#4FACFE" />
    </linearGradient>
    <linearGradient id="purple-glow" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#A855F7" />
      <stop offset="100%" stop-color="#C084FC" />
    </linearGradient>
    <linearGradient id="emerald-glow" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#10B981" />
      <stop offset="100%" stop-color="#34D399" />
    </linearGradient>
    <linearGradient id="amber-glow" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#F59E0B" />
      <stop offset="100%" stop-color="#FBBF24" />
    </linearGradient>
    <filter id="subtle-glow-m" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="2" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>
    <style>
      .metric-num { font-family: 'Inter', system-ui, sans-serif; font-weight: 800; font-size: 28px; }
      .metric-lbl { font-family: 'Inter', system-ui, sans-serif; font-weight: 600; font-size: 12px; fill: #94A3B8; }
      .metric-sub { font-family: 'Inter', system-ui, sans-serif; font-weight: 400; font-size: 11px; fill: #64748B; }
    </style>
  </defs>

  <rect x="2" y="2" width="846" height="161" rx="14" fill="url(#bg-grad-m)" stroke="rgba(255, 255, 255, 0.08)" stroke-width="1.5" />

  <g transform="translate(20, 18)">
    <rect x="0" y="0" width="190" height="128" rx="10" fill="url(#card-grad)" stroke="rgba(0, 242, 254, 0.25)" stroke-width="1" />
    <text x="16" y="42" class="metric-num" fill="url(#cyan-glow)" filter="url(#subtle-glow-m)">103+</text>
    <text x="16" y="68" class="metric-lbl">Live Phone Calls</text>
    <text x="16" y="86" class="metric-sub">Handled in Production</text>
    <text x="16" y="104" class="metric-sub" fill="#00F2FE">• SKAIS Voice AI Agent</text>
  </g>

  <g transform="translate(225, 18)">
    <rect x="0" y="0" width="190" height="128" rx="10" fill="url(#card-grad)" stroke="rgba(168, 85, 247, 0.25)" stroke-width="1" />
    <text x="16" y="42" class="metric-num" fill="url(#purple-glow)" filter="url(#subtle-glow-m)">~50%</text>
    <text x="16" y="68" class="metric-lbl">Monthly Cost Saved</text>
    <text x="16" y="86" class="metric-sub">$1k vs $3k/mo human</text>
    <text x="16" y="104" class="metric-sub" fill="#C084FC">• Automated Phone Staff</text>
  </g>

  <g transform="translate(430, 18)">
    <rect x="0" y="0" width="190" height="128" rx="10" fill="url(#card-grad)" stroke="rgba(16, 185, 129, 0.25)" stroke-width="1" />
    <text x="16" y="42" class="metric-num" fill="url(#emerald-glow)" filter="url(#subtle-glow-m)">100%</text>
    <text x="16" y="68" class="metric-lbl">Manual Typo Removal</text>
    <text x="16" y="86" class="metric-sub">PDF OCR + Diagram AI</text>
    <text x="16" y="104" class="metric-sub" fill="#34D399">• ExamBro Platform</text>
  </g>

  <g transform="translate(635, 18)">
    <rect x="0" y="0" width="195" height="128" rx="10" fill="url(#card-grad)" stroke="rgba(245, 158, 11, 0.25)" stroke-width="1" />
    <text x="16" y="42" class="metric-num" fill="url(#amber-glow)" filter="url(#subtle-glow-m)">7 Months</text>
    <text x="16" y="68" class="metric-lbl">Production Experience</text>
    <text x="16" y="86" class="metric-sub">Cloudus Infotech</text>
    <text x="16" y="104" class="metric-sub" fill="#FBBF24">• Full Lifecycle AI Dev</text>
  </g>
</svg>'''
    with open('assets/ai_metrics.svg', 'w', encoding='utf-8') as f:
        f.write(svg)
    print("Created ai_metrics.svg")

def create_skais_showcase():
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 850 270" width="100%" height="100%">
  <defs>
    <linearGradient id="skais-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0B0F19" />
      <stop offset="100%" stop-color="#0F172A" />
    </linearGradient>
    <linearGradient id="skais-border" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#00F2FE" />
      <stop offset="100%" stop-color="#4FACFE" />
    </linearGradient>
    <linearGradient id="badge-skais" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="rgba(0, 242, 254, 0.2)" />
      <stop offset="100%" stop-color="rgba(79, 172, 254, 0.2)" />
    </linearGradient>
    <style>
      .proj-title { font-family: 'Inter', system-ui, sans-serif; font-weight: 800; font-size: 22px; fill: #FFFFFF; }
      .proj-tagline { font-family: 'Inter', system-ui, sans-serif; font-weight: 600; font-size: 13px; fill: #00F2FE; }
      .flow-box-text { font-family: 'Fira Code', monospace; font-size: 11px; font-weight: 600; fill: #E2E8F0; }
      .flow-sub { font-family: 'Inter', sans-serif; font-size: 10px; fill: #94A3B8; }
      .feat-bullet { font-family: 'Inter', sans-serif; font-size: 12px; fill: #CBD5E1; }
      .tag-text { font-family: 'Fira Code', monospace; font-size: 10px; font-weight: 600; fill: #38BDF8; }
    </style>
  </defs>

  <rect x="2" y="2" width="846" height="266" rx="14" fill="url(#skais-bg)" stroke="url(#skais-border)" stroke-width="1.5" />

  <g transform="translate(24, 20)">
    <text x="0" y="22" class="proj-title">🎙️ SKAIS — Autonomous Restaurant Voice AI Agent</text>
    <rect x="520" y="4" width="120" height="24" rx="12" fill="url(#badge-skais)" stroke="#00F2FE" stroke-width="1" />
    <text x="532" y="20" class="proj-tagline">PRODUCTION AI</text>
  </g>

  <g transform="translate(24, 60)">
    <rect x="0" y="0" width="802" height="76" rx="10" fill="rgba(255, 255, 255, 0.02)" stroke="rgba(255, 255, 255, 0.08)" stroke-width="1" />

    <g transform="translate(16, 14)">
      <rect x="0" y="0" width="120" height="48" rx="6" fill="#1E293B" stroke="#38BDF8" stroke-width="1"/>
      <text x="60" y="22" text-anchor="middle" class="flow-box-text">📞 Customer Call</text>
      <text x="60" y="38" text-anchor="middle" class="flow-sub">Twilio Inbound</text>
    </g>

    <path d="M 142 38 L 168 38" stroke="#00F2FE" stroke-width="1.5" stroke-dasharray="4,2" />
    
    <g transform="translate(174, 14)">
      <rect x="0" y="0" width="140" height="48" rx="6" fill="#1E293B" stroke="#A855F7" stroke-width="1"/>
      <text x="70" y="22" text-anchor="middle" class="flow-box-text">🤖 Retell AI SDK</text>
      <text x="70" y="38" text-anchor="middle" class="flow-sub">Voice &amp; Prompt Logic</text>
    </g>

    <path d="M 320 38 L 346 38" stroke="#A855F7" stroke-width="1.5" stroke-dasharray="4,2" />

    <g transform="translate(352, 14)">
      <rect x="0" y="0" width="140" height="48" rx="6" fill="#1E293B" stroke="#EC4899" stroke-width="1"/>
      <text x="70" y="22" text-anchor="middle" class="flow-box-text">📚 RAG Engine</text>
      <text x="70" y="38" text-anchor="middle" class="flow-sub">FAISS / Vector Search</text>
    </g>

    <path d="M 498 38 L 524 38" stroke="#EC4899" stroke-width="1.5" stroke-dasharray="4,2" />

    <g transform="translate(530, 14)">
      <rect x="0" y="0" width="130" height="48" rx="6" fill="#1E293B" stroke="#10B981" stroke-width="1"/>
      <text x="65" y="22" text-anchor="middle" class="flow-box-text">⚡ FastAPI</text>
      <text x="65" y="38" text-anchor="middle" class="flow-sub">Supabase Backend</text>
    </g>

    <path d="M 666 38 L 690 38" stroke="#10B981" stroke-width="1.5" stroke-dasharray="4,2" />

    <g transform="translate(696, 14)">
      <rect x="0" y="0" width="90" height="48" rx="6" fill="#1E293B" stroke="#F59E0B" stroke-width="1"/>
      <text x="45" y="22" text-anchor="middle" class="flow-box-text">📱 SMS / POS</text>
      <text x="45" y="38" text-anchor="middle" class="flow-sub">Order Placed</text>
    </g>
  </g>

  <g transform="translate(24, 150)">
    <text x="0" y="16" class="feat-bullet">• <tspan font-weight="700" fill="#FFFFFF">Zero Hallucination Guardrails:</tspan> Fine-tuned prompt logic &amp; strict vector RAG base for live call accuracy.</text>
    <text x="0" y="38" class="feat-bullet">• <tspan font-weight="700" fill="#FFFFFF">Real-Time Operations:</tspan> Dynamic price calculation, reservation availability checking &amp; automated Twilio SMS confirmations.</text>
    <text x="0" y="60" class="feat-bullet">• <tspan font-weight="700" fill="#FFFFFF">SaaS Control Center:</tspan> Custom Next.js admin portal for restaurant owners + integrated LangChain customer support chatbot.</text>
  </g>

  <g transform="translate(24, 230)">
    <rect x="0" y="0" width="85" height="22" rx="4" fill="rgba(56, 189, 248, 0.12)" stroke="rgba(56, 189, 248, 0.3)" stroke-width="1" />
    <text x="42" y="15" text-anchor="middle" class="tag-text">Retell AI SDK</text>

    <rect x="95" y="0" width="65" height="22" rx="4" fill="rgba(56, 189, 248, 0.12)" stroke="rgba(56, 189, 248, 0.3)" stroke-width="1" />
    <text x="127" y="15" text-anchor="middle" class="tag-text">FastAPI</text>

    <rect x="170" y="0" width="70" height="22" rx="4" fill="rgba(56, 189, 248, 0.12)" stroke="rgba(56, 189, 248, 0.3)" stroke-width="1" />
    <text x="205" y="15" text-anchor="middle" class="tag-text">Next.js</text>

    <rect x="250" y="0" width="75" height="22" rx="4" fill="rgba(56, 189, 248, 0.12)" stroke="rgba(56, 189, 248, 0.3)" stroke-width="1" />
    <text x="287" y="15" text-anchor="middle" class="tag-text">Supabase</text>

    <rect x="335" y="0" width="80" height="22" rx="4" fill="rgba(56, 189, 248, 0.12)" stroke="rgba(56, 189, 248, 0.3)" stroke-width="1" />
    <text x="375" y="15" text-anchor="middle" class="tag-text">Gemini AI</text>

    <rect x="425" y="0" width="85" height="22" rx="4" fill="rgba(56, 189, 248, 0.12)" stroke="rgba(56, 189, 248, 0.3)" stroke-width="1" />
    <text x="467" y="15" text-anchor="middle" class="tag-text">LangChain</text>

    <rect x="520" y="0" width="80" height="22" rx="4" fill="rgba(56, 189, 248, 0.12)" stroke="rgba(56, 189, 248, 0.3)" stroke-width="1" />
    <text x="560" y="15" text-anchor="middle" class="tag-text">Twilio SDK</text>

    <rect x="610" y="0" width="85" height="22" rx="4" fill="rgba(56, 189, 248, 0.12)" stroke="rgba(56, 189, 248, 0.3)" stroke-width="1" />
    <text x="652" y="15" text-anchor="middle" class="tag-text">Square POS</text>
  </g>
</svg>'''
    with open('assets/skais_showcase.svg', 'w', encoding='utf-8') as f:
        f.write(svg)
    print("Created skais_showcase.svg")

def create_exambro_showcase():
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 850 270" width="100%" height="100%">
  <defs>
    <linearGradient id="exam-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0B0F19" />
      <stop offset="100%" stop-color="#0F172A" />
    </linearGradient>
    <linearGradient id="exam-border" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#A855F7" />
      <stop offset="100%" stop-color="#EC4899" />
    </linearGradient>
    <linearGradient id="badge-exam" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="rgba(168, 85, 247, 0.2)" />
      <stop offset="100%" stop-color="rgba(236, 72, 153, 0.2)" />
    </linearGradient>
    <style>
      .proj-title { font-family: 'Inter', system-ui, sans-serif; font-weight: 800; font-size: 22px; fill: #FFFFFF; }
      .proj-tagline { font-family: 'Inter', system-ui, sans-serif; font-weight: 600; font-size: 13px; fill: #C084FC; }
      .flow-box-text { font-family: 'Fira Code', monospace; font-size: 11px; font-weight: 600; fill: #E2E8F0; }
      .flow-sub { font-family: 'Inter', sans-serif; font-size: 10px; fill: #94A3B8; }
      .feat-bullet { font-family: 'Inter', sans-serif; font-size: 12px; fill: #CBD5E1; }
      .tag-text { font-family: 'Fira Code', monospace; font-size: 10px; font-weight: 600; fill: #C084FC; }
    </style>
  </defs>

  <rect x="2" y="2" width="846" height="266" rx="14" fill="url(#exam-bg)" stroke="url(#exam-border)" stroke-width="1.5" />

  <g transform="translate(24, 20)">
    <text x="0" y="22" class="proj-title">📄 ExamBro — Intelligent OCR &amp; Exam Management Platform</text>
    <rect x="590" y="4" width="135" height="24" rx="12" fill="url(#badge-exam)" stroke="#A855F7" stroke-width="1" />
    <text x="602" y="20" class="proj-tagline">AI OCR ENGINE</text>
  </g>

  <g transform="translate(24, 60)">
    <rect x="0" y="0" width="802" height="76" rx="10" fill="rgba(255, 255, 255, 0.02)" stroke="rgba(255, 255, 255, 0.08)" stroke-width="1" />

    <g transform="translate(16, 14)">
      <rect x="0" y="0" width="125" height="48" rx="6" fill="#1E293B" stroke="#C084FC" stroke-width="1"/>
      <text x="62" y="22" text-anchor="middle" class="flow-box-text">📑 Teacher PDF</text>
      <text x="62" y="38" text-anchor="middle" class="flow-sub">Exam / Question Paper</text>
    </g>

    <path d="M 147 38 L 173 38" stroke="#C084FC" stroke-width="1.5" stroke-dasharray="4,2" />
    
    <g transform="translate(179, 14)">
      <rect x="0" y="0" width="145" height="48" rx="6" fill="#1E293B" stroke="#EC4899" stroke-width="1"/>
      <text x="72" y="22" text-anchor="middle" class="flow-box-text">🔍 Mistral OCR</text>
      <text x="72" y="38" text-anchor="middle" class="flow-sub">PyMuPDF &amp; OpenCV</text>
    </g>

    <path d="M 330 38 L 356 38" stroke="#EC4899" stroke-width="1.5" stroke-dasharray="4,2" />

    <g transform="translate(362, 14)">
      <rect x="0" y="0" width="145" height="48" rx="6" fill="#1E293B" stroke="#38BDF8" stroke-width="1"/>
      <text x="72" y="22" text-anchor="middle" class="flow-box-text">✨ Gemini LLM</text>
      <text x="72" y="38" text-anchor="middle" class="flow-sub">Structured JSON Output</text>
    </g>

    <path d="M 513 38 L 539 38" stroke="#38BDF8" stroke-width="1.5" stroke-dasharray="4,2" />

    <g transform="translate(545, 14)">
      <rect x="0" y="0" width="125" height="48" rx="6" fill="#1E293B" stroke="#10B981" stroke-width="1"/>
      <text x="62" y="22" text-anchor="middle" class="flow-box-text">🐳 Dockerized API</text>
      <text x="62" y="38" text-anchor="middle" class="flow-sub">Django &amp; FastAPI</text>
    </g>

    <path d="M 676 38 L 700 38" stroke="#10B981" stroke-width="1.5" stroke-dasharray="4,2" />

    <g transform="translate(706, 14)">
      <rect x="0" y="0" width="80" height="48" rx="6" fill="#1E293B" stroke="#F59E0B" stroke-width="1"/>
      <text x="40" y="22" text-anchor="middle" class="flow-box-text">🖥️ Portal</text>
      <text x="40" y="38" text-anchor="middle" class="flow-sub">Question Bank</text>
    </g>
  </g>

  <g transform="translate(24, 150)">
    <text x="0" y="16" class="feat-bullet">• <tspan font-weight="700" fill="#FFFFFF">Diagram Alignment Fix:</tspan> Resolved image shifting bug during PDF extraction using OpenCV spatial bounding boxes.</text>
    <text x="0" y="38" class="feat-bullet">• <tspan font-weight="700" fill="#FFFFFF">Smart Auto-Filling:</tspan> Employed Gemini LLM to parse unformatted text, auto-extract options, and compute missing solutions.</text>
    <text x="0" y="60" class="feat-bullet">• <tspan font-weight="700" fill="#FFFFFF">Multilingual &amp; Scalable:</tspan> Built bulk question management admin panel with multi-language translation support.</text>
  </g>

  <g transform="translate(24, 230)">
    <rect x="0" y="0" width="65" height="22" rx="4" fill="rgba(168, 85, 247, 0.12)" stroke="rgba(168, 85, 247, 0.3)" stroke-width="1" />
    <text x="32" y="15" text-anchor="middle" class="tag-text">Python</text>

    <rect x="75" y="0" width="65" height="22" rx="4" fill="rgba(168, 85, 247, 0.12)" stroke="rgba(168, 85, 247, 0.3)" stroke-width="1" />
    <text x="107" y="15" text-anchor="middle" class="tag-text">Django</text>

    <rect x="150" y="0" width="65" height="22" rx="4" fill="rgba(168, 85, 247, 0.12)" stroke="rgba(168, 85, 247, 0.3)" stroke-width="1" />
    <text x="182" y="15" text-anchor="middle" class="tag-text">FastAPI</text>

    <rect x="225" y="0" width="90" height="22" rx="4" fill="rgba(168, 85, 247, 0.12)" stroke="rgba(168, 85, 247, 0.3)" stroke-width="1" />
    <text x="270" y="15" text-anchor="middle" class="tag-text">Mistral OCR</text>

    <rect x="325" y="0" width="80" height="22" rx="4" fill="rgba(168, 85, 247, 0.12)" stroke="rgba(168, 85, 247, 0.3)" stroke-width="1" />
    <text x="365" y="15" text-anchor="middle" class="tag-text">PyMuPDF</text>

    <rect x="415" y="0" width="70" height="22" rx="4" fill="rgba(168, 85, 247, 0.12)" stroke="rgba(168, 85, 247, 0.3)" stroke-width="1" />
    <text x="450" y="15" text-anchor="middle" class="tag-text">OpenCV</text>

    <rect x="495" y="0" width="80" height="22" rx="4" fill="rgba(168, 85, 247, 0.12)" stroke="rgba(168, 85, 247, 0.3)" stroke-width="1" />
    <text x="535" y="15" text-anchor="middle" class="tag-text">Gemini AI</text>

    <rect x="585" y="0" width="65" height="22" rx="4" fill="rgba(168, 85, 247, 0.12)" stroke="rgba(168, 85, 247, 0.3)" stroke-width="1" />
    <text x="617" y="15" text-anchor="middle" class="tag-text">Docker</text>
  </g>
</svg>'''
    with open('assets/exambro_showcase.svg', 'w', encoding='utf-8') as f:
        f.write(svg)
    print("Created exambro_showcase.svg")

def create_skills_radar():
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 850 280" width="100%" height="100%">
  <defs>
    <linearGradient id="skills-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0B0F19" />
      <stop offset="100%" stop-color="#111827" />
    </linearGradient>
    
    <linearGradient id="bar-grad-1" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#00F2FE" />
      <stop offset="100%" stop-color="#4FACFE" />
    </linearGradient>
    
    <linearGradient id="bar-grad-2" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#A855F7" />
      <stop offset="100%" stop-color="#C084FC" />
    </linearGradient>

    <linearGradient id="bar-grad-3" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#10B981" />
      <stop offset="100%" stop-color="#34D399" />
    </linearGradient>
    
    <style>
      .sec-header { font-family: 'Inter', system-ui, sans-serif; font-weight: 800; font-size: 18px; fill: #FFFFFF; }
      .skill-label { font-family: 'Inter', system-ui, sans-serif; font-weight: 600; font-size: 13px; fill: #E2E8F0; }
      .skill-percent { font-family: 'Fira Code', monospace; font-size: 12px; font-weight: 700; fill: #94A3B8; }
      .skill-desc { font-family: 'Inter', sans-serif; font-size: 11px; fill: #64748B; }
    </style>
  </defs>

  <rect x="2" y="2" width="846" height="276" rx="14" fill="url(#skills-bg)" stroke="rgba(255, 255, 255, 0.08)" stroke-width="1.5" />

  <text x="24" y="34" class="sec-header">📊 Technical Architecture &amp; Core Mastery</text>

  <g transform="translate(24, 60)">
    <g transform="translate(0, 0)">
      <text x="0" y="14" class="skill-label">LLM Applications &amp; Generative AI</text>
      <text x="360" y="14" text-anchor="end" class="skill-percent">95%</text>
      <text x="0" y="30" class="skill-desc">Prompt Engineering, OpenAI API, Gemini API, Claude API, Transformers</text>
      <rect x="0" y="36" width="360" height="8" rx="4" fill="rgba(255,255,255,0.06)" />
      <rect x="0" y="36" width="342" height="8" rx="4" fill="url(#bar-grad-1)" />
    </g>

    <g transform="translate(0, 62)">
      <text x="0" y="14" class="skill-label">RAG Pipelines &amp; Vector Search</text>
      <text x="360" y="14" text-anchor="end" class="skill-percent">92%</text>
      <text x="0" y="30" class="skill-desc">FAISS, Pinecone, Embeddings, Dynamic Chunking Strategies</text>
      <rect x="0" y="36" width="360" height="8" rx="4" fill="rgba(255,255,255,0.06)" />
      <rect x="0" y="36" width="331" height="8" rx="4" fill="url(#bar-grad-1)" />
    </g>

    <g transform="translate(0, 124)">
      <text x="0" y="14" class="skill-label">AI Agents &amp; Multi-Agent Workflows</text>
      <text x="360" y="14" text-anchor="end" class="skill-percent">90%</text>
      <text x="0" y="30" class="skill-desc">LangChain, LangGraph, Google ADK, Retell AI SDK, MCP, Function Calling</text>
      <rect x="0" y="36" width="360" height="8" rx="4" fill="rgba(255,255,255,0.06)" />
      <rect x="0" y="36" width="324" height="8" rx="4" fill="url(#bar-grad-1)" />
    </g>
  </g>

  <g transform="translate(440, 60)">
    <g transform="translate(0, 0)">
      <text x="0" y="14" class="skill-label">Backend Architecture &amp; REST APIs</text>
      <text x="385" y="14" text-anchor="end" class="skill-percent">90%</text>
      <text x="0" y="30" class="skill-desc">FastAPI, Django, Python Async, Twilio SDK, Supabase</text>
      <rect x="0" y="36" width="385" height="8" rx="4" fill="rgba(255,255,255,0.06)" />
      <rect x="0" y="36" width="346" height="8" rx="4" fill="url(#bar-grad-2)" />
    </g>

    <g transform="translate(0, 62)">
      <text x="0" y="14" class="skill-label">OCR &amp; Document Intelligence</text>
      <text x="385" y="14" text-anchor="end" class="skill-percent">88%</text>
      <text x="0" y="30" class="skill-desc">Mistral OCR, PyMuPDF, OpenCV, Image Alignment, PDF Parsing</text>
      <rect x="0" y="36" width="385" height="8" rx="4" fill="rgba(255,255,255,0.06)" />
      <rect x="0" y="36" width="338" height="8" rx="4" fill="url(#bar-grad-2)" />
    </g>

    <g transform="translate(0, 124)">
      <text x="0" y="14" class="skill-label">Cloud, DevOps &amp; Databases</text>
      <text x="385" y="14" text-anchor="end" class="skill-percent">85%</text>
      <text x="0" y="30" class="skill-desc">AWS, Docker, PostgreSQL, Supabase, MongoDB, Git/GitHub</text>
      <rect x="0" y="36" width="385" height="8" rx="4" fill="rgba(255,255,255,0.06)" />
      <rect x="0" y="36" width="327" height="8" rx="4" fill="url(#bar-grad-3)" />
    </g>
  </g>
</svg>'''
    with open('assets/skills_radar.svg', 'w', encoding='utf-8') as f:
        f.write(svg)
    print("Created skills_radar.svg")

if __name__ == '__main__':
    os.makedirs('assets', exist_ok=True)
    create_hero_banner()
    create_ai_metrics()
    create_skais_showcase()
    create_exambro_showcase()
    create_skills_radar()
    print("All 5 SVG assets created successfully!")
