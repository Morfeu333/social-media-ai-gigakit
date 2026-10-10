import re

def update_page(filepath, is_en=False):
    with open(filepath, "r", encoding="utf-8") as f:
        html = f.read()

    # 1. Update Buttons linking to #precos or #diagnostico to trigger openQuizModal()
    # Replace href="#precos" in hero CTA and header
    html = html.replace('href="#precos"', 'href="javascript:void(0)" onclick="openQuizModal()"')
    html = html.replace('href="#diagnostico"', 'href="javascript:void(0)" onclick="openQuizModal()"')

    # 2. Add Modal CSS
    modal_css = """
    /* QUIZ MODAL OVERLAY & POPUP */
    .quiz-modal-overlay {
      position: fixed;
      inset: 0;
      background: rgba(2, 11, 30, 0.88);
      backdrop-filter: blur(16px);
      z-index: 9999;
      display: none;
      align-items: center;
      justify-content: center;
      padding: 20px;
      overflow-y: auto;
    }
    .quiz-modal-overlay.active {
      display: flex;
      animation: fadeInModal 0.25s ease forwards;
    }
    .quiz-modal-container {
      background: rgba(4, 25, 65, 0.95);
      border: 1px solid rgba(0, 240, 255, 0.45);
      box-shadow: 0 0 80px rgba(13, 98, 254, 0.5), inset 0 0 40px rgba(0, 240, 255, 0.08);
      border-radius: 24px;
      max-width: 820px;
      width: 100%;
      padding: 36px 32px;
      position: relative;
      margin: auto;
    }
    .quiz-modal-close {
      position: absolute;
      top: 20px;
      right: 20px;
      background: rgba(255, 255, 255, 0.08);
      border: 1px solid rgba(255, 255, 255, 0.15);
      color: #93C5FD;
      width: 36px;
      height: 36px;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      font-size: 1.2rem;
      transition: all 0.2s;
    }
    .quiz-modal-close:hover {
      background: rgba(255, 45, 117, 0.2);
      border-color: #FF2D75;
      color: #FFF;
    }
    .quiz-modal-offers {
      margin-top: 28px;
      border-top: 1px solid rgba(0, 240, 255, 0.2);
      padding-top: 28px;
      display: none;
    }
    .quiz-modal-offers.active {
      display: block;
      animation: fadeInModal 0.35s ease forwards;
    }
    .modal-offers-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 16px;
      margin-top: 20px;
    }
    @media (max-width: 780px) {
      .modal-offers-grid {
        grid-template-columns: 1fr;
      }
    }
    .modal-offer-card {
      background: rgba(3, 20, 50, 0.8);
      border: 1px solid rgba(0, 240, 255, 0.25);
      border-radius: 14px;
      padding: 20px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      transition: all 0.2s;
      position: relative;
    }
    .modal-offer-card:hover {
      border-color: var(--cyan);
      box-shadow: 0 0 25px rgba(0, 240, 255, 0.2);
      transform: translateY(-2px);
    }
    .modal-offer-card.recommended {
      border-color: var(--cyan);
      background: linear-gradient(180deg, rgba(13, 98, 254, 0.25) 0%, rgba(3, 20, 50, 0.9) 100%);
      box-shadow: 0 0 35px rgba(0, 240, 255, 0.25);
    }
    .modal-badge-rec {
      position: absolute;
      top: -11px;
      left: 50%;
      transform: translateX(-50%);
      background: var(--cyan);
      color: #020B1E;
      font-size: 0.65rem;
      font-weight: 800;
      padding: 2px 10px;
      border-radius: 100px;
      letter-spacing: 0.05em;
    }
    @keyframes fadeInModal {
      from { opacity: 0; transform: scale(0.97); }
      to { opacity: 1; transform: scale(1); }
    }
    """

    if ".quiz-modal-overlay" not in html:
        html = html.replace("</style>", modal_css + "\n</style>")

    # 3. Add Modal HTML Structure before </body>
    modal_html_pt = """
  <!-- POPUP QUIZ MODAL WITH 3 OFFERS ALWAYS REVEALED -->
  <div id="quizModal" class="quiz-modal-overlay">
    <div class="quiz-modal-container">
      <button class="quiz-modal-close" onclick="closeQuizModal()">&times;</button>
      
      <div id="modalQuizContent">
        <div class="section-title-wrap" style="margin-bottom: 24px;">
          <span class="section-tag">DIAGNÓSTICO PERSONALIZADO</span>
          <h2 class="section-title" style="font-size: 1.6rem; margin-bottom: 6px;">Qual é o Seu Momento Atual com IA?</h2>
          <p class="section-desc" style="font-size: 0.88rem;">
            Responda 3 perguntas rápidas para calibrar sua recomendação personalizada:
          </p>
        </div>

        <!-- PERGUNTA 1 -->
        <div id="m-quiz-step-1">
          <span class="quiz-step-tag">PERGUNTA 1 DE 3</span>
          <h3 class="quiz-question" style="font-size: 1.15rem;">Qual é o seu objetivo imediato de produção?</h3>
          <div class="quiz-options">
            <button onclick="handleModalQuiz(1, 'vault')" class="quiz-opt-btn">
              <span>Quero o Vault de códigos, repositórios, skills e MCPs prontos para usar no meu ritmo.</span>
              <span class="quiz-opt-arrow">&rarr;</span>
            </button>
            <button onclick="handleModalQuiz(1, 'group')" class="quiz-opt-btn">
              <span>Quero chamadas ao vivo 3x por semana em grupo para acelerar e destravar projetos na tela.</span>
              <span class="quiz-opt-arrow">&rarr;</span>
            </button>
            <button onclick="handleModalQuiz(1, 'mentorship')" class="quiz-opt-btn">
              <span>Quero mentoria individual 1:1 com auditoria direta e acompanhamento das minhas contas.</span>
              <span class="quiz-opt-arrow">&rarr;</span>
            </button>
          </div>
        </div>

        <!-- PERGUNTA 2 -->
        <div id="m-quiz-step-2" style="display: none;">
          <span class="quiz-step-tag">PERGUNTA 2 DE 3</span>
          <h3 class="quiz-question" style="font-size: 1.15rem;">Qual o seu foco de mercado e monetização?</h3>
          <div class="quiz-options">
            <button onclick="handleModalQuiz(2, 'us')" class="quiz-opt-btn">
              <span>Foco em faturamento em Dólar (USD) atendendo marcas e canais gringos.</span>
              <span class="quiz-opt-arrow">&rarr;</span>
            </button>
            <button onclick="handleModalQuiz(2, 'br')" class="quiz-opt-btn">
              <span>Foco em consolidar audiência e autoridade no mercado brasileiro primeiro.</span>
              <span class="quiz-opt-arrow">&rarr;</span>
            </button>
          </div>
        </div>

        <!-- PERGUNTA 3 -->
        <div id="m-quiz-step-3" style="display: none;">
          <span class="quiz-step-tag">PERGUNTA 3 DE 3</span>
          <h3 class="quiz-question" style="font-size: 1.15rem;">Qual formato de suporte você mais valoriza?</h3>
          <div class="quiz-options">
            <button onclick="handleModalQuiz(3, 'async')" class="quiz-opt-btn">
              <span>Suporte ágil direto no WhatsApp VIP e materiais arquivados no Facebook.</span>
              <span class="quiz-opt-arrow">&rarr;</span>
            </button>
            <button onclick="handleModalQuiz(3, 'sync')" class="quiz-opt-btn">
              <span>Sessões interativas de plantão técnico com compartilhamento de tela.</span>
              <span class="quiz-opt-arrow">&rarr;</span>
            </button>
          </div>
        </div>
      </div>

      <!-- AS 3 OFERTAS APARECEM SEMPRE ABAIXO AO COMPLETAR O QUIZ -->
      <div id="modalOffersSection" class="quiz-modal-offers">
        <div style="text-align: center; margin-bottom: 12px;">
          <div class="quiz-check-icon" style="width: 44px; height: 44px; font-size: 1.2rem; margin-bottom: 10px;">✓</div>
          <span class="quiz-step-tag">DIAGNÓSTICO CONCLUÍDO</span>
          <h3 id="modalRecHeadline" style="font-size: 1.3rem; color: #FFF; font-weight: 800; margin-bottom: 4px;">Opções Disponíveis para o Seu Perfil</h3>
          <p id="modalRecSubtext" style="color: var(--text-muted); font-size: 0.85rem; max-width: 580px; margin: 0 auto;"></p>
        </div>

        <div class="modal-offers-grid">
          <!-- TIER 1 -->
          <div class="modal-offer-card" id="cardTier1">
            <div>
              <span style="font-family: var(--font-mono); font-size: 0.7rem; color: var(--cyan); font-weight: 700;">TIER 1 · AUTO-DIDATA</span>
              <h4 style="color: #FFF; font-size: 1.1rem; margin: 4px 0 8px;">Vault Member</h4>
              <p style="color: var(--text-muted); font-size: 0.78rem; line-height: 1.4; margin-bottom: 12px;">
                Acesso a todos os repositórios, skills, templates GHL e grupo VIP no WhatsApp + Facebook.
              </p>
              <div style="font-family: var(--font-mono); font-size: 1.35rem; font-weight: 800; color: #FFF; margin-bottom: 14px;">
                $30 <span style="font-size: 0.75rem; color: var(--text-dim); font-weight: 500;">/ mês</span>
              </div>
            </div>
            <a href="https://buy.stripe.com/8x2cN410Q35mczm2MU0Ny0f" class="btn-buy primary" style="padding: 10px; font-size: 0.85rem; width: 100%; text-align: center;">
              Assinar Vault ($30/mês) &rarr;
            </a>
          </div>

          <!-- TIER 2 -->
          <div class="modal-offer-card recommended" id="cardTier2">
            <span class="modal-badge-rec">MAIS ESCOLHIDO</span>
            <div>
              <span style="font-family: var(--font-mono); font-size: 0.7rem; color: var(--cyan); font-weight: 700;">TIER 2 · ACELERADOR</span>
              <h4 style="color: #FFF; font-size: 1.1rem; margin: 4px 0 8px;">Acelerador Pro</h4>
              <p style="color: var(--text-muted); font-size: 0.78rem; line-height: 1.4; margin-bottom: 12px;">
                Vault completo + 3 Encontros ao vivo semanais em grupo tirando dúvidas direto na tela.
              </p>
              <div style="font-family: var(--font-mono); font-size: 1.35rem; font-weight: 800; color: #FFF; margin-bottom: 14px;">
                $90 <span style="font-size: 0.75rem; color: var(--text-dim); font-weight: 500;">/ mês</span>
              </div>
            </div>
            <a href="https://buy.stripe.com/dRmaEW24U49qczmfzG0Ny0g" class="btn-buy accent" style="padding: 10px; font-size: 0.85rem; width: 100%; text-align: center;">
              Entrar Pro ($90/mês) &rarr;
            </a>
          </div>

          <!-- TIER 3 -->
          <div class="modal-offer-card" id="cardTier3">
            <div>
              <span style="font-family: var(--font-mono); font-size: 0.7rem; color: var(--cyan); font-weight: 700;">TIER 3 · INDIVIDUAL</span>
              <h4 style="color: #FFF; font-size: 1.1rem; margin: 4px 0 8px;">Mentoria 1:1 VIP</h4>
              <p style="color: var(--text-muted); font-size: 0.78rem; line-height: 1.4; margin-bottom: 12px;">
                Acompanhamento pessoal com Lucas, 2 calls semanais individuais, auditoria de CRM e campanhas.
              </p>
              <div style="font-family: var(--font-mono); font-size: 1.35rem; font-weight: 800; color: #FFF; margin-bottom: 14px;">
                $3.000 <span style="font-size: 0.75rem; color: var(--text-dim); font-weight: 500;">/ 3 meses</span>
              </div>
            </div>
            <a href="https://buy.stripe.com/aFa6oGdNCeO47f2dry0Ny0h" class="btn-buy primary" style="padding: 10px; font-size: 0.85rem; width: 100%; text-align: center;">
              Vaga Individual ($3k) &rarr;
            </a>
          </div>
        </div>
      </div>
    </div>
  </div>
    """

    modal_html_en = """
  <!-- POPUP QUIZ MODAL WITH 3 OFFERS ALWAYS REVEALED -->
  <div id="quizModal" class="quiz-modal-overlay">
    <div class="quiz-modal-container">
      <button class="quiz-modal-close" onclick="closeQuizModal()">&times;</button>
      
      <div id="modalQuizContent">
        <div class="section-title-wrap" style="margin-bottom: 24px;">
          <span class="section-tag">CUSTOM DIAGNOSTIC</span>
          <h2 class="section-title" style="font-size: 1.6rem; margin-bottom: 6px;">What Is Your Current AI Social Media Stage?</h2>
          <p class="section-desc" style="font-size: 0.88rem;">
            Answer 3 quick questions to calibrate your tailored recommendation:
          </p>
        </div>

        <!-- QUESTION 1 -->
        <div id="m-quiz-step-1">
          <span class="quiz-step-tag">QUESTION 1 OF 3</span>
          <h3 class="quiz-question" style="font-size: 1.15rem;">What is your immediate production objective?</h3>
          <div class="quiz-options">
            <button onclick="handleModalQuiz(1, 'vault')" class="quiz-opt-btn">
              <span>I want the ready-to-use codebase, repos, skills and MCPs to build at my own pace.</span>
              <span class="quiz-opt-arrow">&rarr;</span>
            </button>
            <button onclick="handleModalQuiz(1, 'group')" class="quiz-opt-btn">
              <span>I want 3x weekly live coaching calls in group to unblock projects on screen.</span>
              <span class="quiz-opt-arrow">&rarr;</span>
            </button>
            <button onclick="handleModalQuiz(1, 'mentorship')" class="quiz-opt-btn">
              <span>I want direct 1:1 individual mentorship with complete account audit and setup.</span>
              <span class="quiz-opt-arrow">&rarr;</span>
            </button>
          </div>
        </div>

        <!-- QUESTION 2 -->
        <div id="m-quiz-step-2" style="display: none;">
          <span class="quiz-step-tag">QUESTION 2 OF 3</span>
          <h3 class="quiz-question" style="font-size: 1.15rem;">What is your target market?</h3>
          <div class="quiz-options">
            <button onclick="handleModalQuiz(2, 'us')" class="quiz-opt-btn">
              <span>Earning in US Dollars (USD) managing high-ticket brands and US content.</span>
              <span class="quiz-opt-arrow">&rarr;</span>
            </button>
            <button onclick="handleModalQuiz(2, 'br')" class="quiz-opt-btn">
              <span>Scaling local brands and personal projects first.</span>
              <span class="quiz-opt-arrow">&rarr;</span>
            </button>
          </div>
        </div>

        <!-- QUESTION 3 -->
        <div id="m-quiz-step-3" style="display: none;">
          <span class="quiz-step-tag">QUESTION 3 OF 3</span>
          <h3 class="quiz-question" style="font-size: 1.15rem;">Which support style suits you best?</h3>
          <div class="quiz-options">
            <button onclick="handleModalQuiz(3, 'async')" class="quiz-opt-btn">
              <span>Instant async support via VIP WhatsApp + private Facebook repository.</span>
              <span class="quiz-opt-arrow">&rarr;</span>
            </button>
            <button onclick="handleModalQuiz(3, 'sync')" class="quiz-opt-btn">
              <span>Interactive live working sessions with direct screen share review.</span>
              <span class="quiz-opt-arrow">&rarr;</span>
            </button>
          </div>
        </div>
      </div>

      <!-- 3 OFFERS ALWAYS SHOWN BELOW QUIZ -->
      <div id="modalOffersSection" class="quiz-modal-offers">
        <div style="text-align: center; margin-bottom: 12px;">
          <div class="quiz-check-icon" style="width: 44px; height: 44px; font-size: 1.2rem; margin-bottom: 10px;">✓</div>
          <span class="quiz-step-tag">DIAGNOSTIC COMPLETE</span>
          <h3 id="modalRecHeadline" style="font-size: 1.3rem; color: #FFF; font-weight: 800; margin-bottom: 4px;">Available Tiers for Your Profile</h3>
          <p id="modalRecSubtext" style="color: var(--text-muted); font-size: 0.85rem; max-width: 580px; margin: 0 auto;"></p>
        </div>

        <div class="modal-offers-grid">
          <!-- TIER 1 -->
          <div class="modal-offer-card" id="cardTier1">
            <div>
              <span style="font-family: var(--font-mono); font-size: 0.7rem; color: var(--cyan); font-weight: 700;">TIER 1 · BUILDER</span>
              <h4 style="color: #FFF; font-size: 1.1rem; margin: 4px 0 8px;">Vault Member</h4>
              <p style="color: var(--text-muted); font-size: 0.78rem; line-height: 1.4; margin-bottom: 12px;">
                Full access to all repos, skills, GHL workflows, and VIP WhatsApp + Facebook groups.
              </p>
              <div style="font-family: var(--font-mono); font-size: 1.35rem; font-weight: 800; color: #FFF; margin-bottom: 14px;">
                $30 <span style="font-size: 0.75rem; color: var(--text-dim); font-weight: 500;">/ mo</span>
              </div>
            </div>
            <a href="https://buy.stripe.com/8x2cN410Q35mczm2MU0Ny0f" class="btn-buy primary" style="padding: 10px; font-size: 0.85rem; width: 100%; text-align: center;">
              Get Vault Access ($30/mo) &rarr;
            </a>
          </div>

          <!-- TIER 2 -->
          <div class="modal-offer-card recommended" id="cardTier2">
            <span class="modal-badge-rec">MOST POPULAR</span>
            <div>
              <span style="font-family: var(--font-mono); font-size: 0.7rem; color: var(--cyan); font-weight: 700;">TIER 2 · ACCELERATOR</span>
              <h4 style="color: #FFF; font-size: 1.1rem; margin: 4px 0 8px;">Pro Accelerator</h4>
              <p style="color: var(--text-muted); font-size: 0.78rem; line-height: 1.4; margin-bottom: 12px;">
                Complete Vault + 3 Live weekly group working calls with live problem solving on screen.
              </p>
              <div style="font-family: var(--font-mono); font-size: 1.35rem; font-weight: 800; color: #FFF; margin-bottom: 14px;">
                $90 <span style="font-size: 0.75rem; color: var(--text-dim); font-weight: 500;">/ mo</span>
              </div>
            </div>
            <a href="https://buy.stripe.com/dRmaEW24U49qczmfzG0Ny0g" class="btn-buy accent" style="padding: 10px; font-size: 0.85rem; width: 100%; text-align: center;">
              Join Accelerator ($90/mo) &rarr;
            </a>
          </div>

          <!-- TIER 3 -->
          <div class="modal-offer-card" id="cardTier3">
            <div>
              <span style="font-family: var(--font-mono); font-size: 0.7rem; color: var(--cyan); font-weight: 700;">TIER 3 · 1-ON-1</span>
              <h4 style="color: #FFF; font-size: 1.1rem; margin: 4px 0 8px;">1:1 VIP Mentorship</h4>
              <p style="color: var(--text-muted); font-size: 0.78rem; line-height: 1.4; margin-bottom: 12px;">
                Personal 1-on-1 coaching with Lucas, 2 weekly private calls, CRM and pipeline audit.
              </p>
              <div style="font-family: var(--font-mono); font-size: 1.35rem; font-weight: 800; color: #FFF; margin-bottom: 14px;">
                $3,000 <span style="font-size: 0.75rem; color: var(--text-dim); font-weight: 500;">/ 3 mo</span>
              </div>
            </div>
            <a href="https://buy.stripe.com/aFa6oGdNCeO47f2dry0Ny0h" class="btn-buy primary" style="padding: 10px; font-size: 0.85rem; width: 100%; text-align: center;">
              Claim 1:1 Spot ($3k) &rarr;
            </a>
          </div>
        </div>
      </div>
    </div>
  </div>
    """

    target_modal_html = modal_html_en if is_en else modal_html_pt
    if "id=\"quizModal\"" not in html:
        html = html.replace("</body>", target_modal_html + "\n</body>")

    # 4. Add JS handlers for modal quiz
    modal_js = """
    let mQuizAnswers = {};

    function openQuizModal() {
      const modal = document.getElementById('quizModal');
      if (modal) {
        modal.classList.add('active');
        document.body.style.overflow = 'hidden';
      }
    }

    function closeQuizModal() {
      const modal = document.getElementById('quizModal');
      if (modal) {
        modal.classList.remove('active');
        document.body.style.overflow = '';
      }
    }

    function handleModalQuiz(step, val) {
      mQuizAnswers[step] = val;
      const currentStepEl = document.getElementById('m-quiz-step-' + step);
      if (currentStepEl) currentStepEl.style.display = 'none';

      if (step < 3) {
        const nextStepEl = document.getElementById('m-quiz-step-' + (step + 1));
        if (nextStepEl) nextStepEl.style.display = 'block';
      } else {
        // Quiz completed -> ALWAYS SHOW ALL 3 OFFERS BELOW!
        const offersSec = document.getElementById('modalOffersSection');
        const headline = document.getElementById('modalRecHeadline');
        const subtext = document.getElementById('modalRecSubtext');
        
        // Highlight the matched tier based on answers
        const card1 = document.getElementById('cardTier1');
        const card2 = document.getElementById('cardTier2');
        const card3 = document.getElementById('cardTier3');
        
        [card1, card2, card3].forEach(c => {
          if (c) c.classList.remove('recommended');
        });

        if (mQuizAnswers[1] === 'mentorship') {
          if (card3) card3.classList.add('recommended');
          headline.innerText = '""" + ("Recomendação: Tier 3 (Mentoria 1:1 VIP)" if not is_en else "Recommended: Tier 3 (1:1 VIP Mentorship)") + """';
          subtext.innerText = '""" + ("Seu perfil pede aceleração máxima e acompanhamento individual direto com o Lucas." if not is_en else "Your profile calls for direct private acceleration and audit directly with Lucas.") + """';
        } else if (mQuizAnswers[1] === 'group') {
          if (card2) card2.classList.add('recommended');
          headline.innerText = '""" + ("Recomendação: Tier 2 (Acelerador Pro)" if not is_en else "Recommended: Tier 2 (Pro Accelerator)") + """';
          subtext.innerText = '""" + ("Ideal para destravar projetos e tirar dúvidas na tela 3x por semana em grupo." if not is_en else "Ideal to build and unblock live projects on screen 3x a week in group.") + """';
        } else {
          if (card1) card1.classList.add('recommended');
          headline.innerText = '""" + ("Recomendação: Tier 1 (Vault Member)" if not is_en else "Recommended: Tier 1 (Vault Member)") + """';
          subtext.innerText = '""" + ("Perfeito para implementar no seu ritmo com todo o Vault de códigos e suporte no WhatsApp." if not is_en else "Perfect to implement autonomously with all repos, code and WhatsApp community.") + """';
        }

        if (offersSec) offersSec.classList.add('active');
      }
    }

    // Close on backdrop click
    document.addEventListener('click', function(e) {
      const modal = document.getElementById('quizModal');
      if (modal && e.target === modal) {
        closeQuizModal();
      }
    });
    """

    if "function openQuizModal" not in html:
        html = html.replace("</script>", modal_js + "\n</script>")

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)
    print("Updated quiz modal in", filepath)

update_page("/home/automatrix/Projects/social-media-ai-gigakit/public/index.html", is_en=False)
update_page("/home/automatrix/Projects/social-media-ai-gigakit/public/en.html", is_en=True)
