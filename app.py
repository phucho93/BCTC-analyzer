import streamlit as st
import json
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots

st.set_page_config(
    page_title="BCTC Analyzer Pro",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
.main-header {
    background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
    padding: 1.8rem 2rem; border-radius: 12px;
    margin-bottom: 1.5rem; color: white;
}
.main-header h1 { margin: 0; font-size: 1.8rem; font-weight: 700; }
.main-header p { margin: 0.4rem 0 0; opacity: 0.75; font-size: 0.95rem; }
.metric-card {
    background: white; border: 1px solid #e2e8f0;
    border-radius: 10px; padding: 1rem 1.2rem;
    text-align: center; box-shadow: 0 2px 6px rgba(0,0,0,0.05);
}
.metric-val { font-size: 1.7rem; font-weight: 700; color: #1a202c; }
.metric-lbl { font-size: 0.75rem; color: #718096; margin-top: 3px; text-transform: uppercase; letter-spacing: 0.04em; }
.metric-chg-pos { color: #38a169; font-size: 0.85rem; font-weight: 600; }
.metric-chg-neg { color: #e53e3e; font-size: 0.85rem; font-weight: 600; }
.section-header { font-size: 1.1rem; font-weight: 600; color: #2d3748; margin: 1.2rem 0 0.8rem; border-left: 4px solid #3182ce; padding-left: 0.8rem; }
.flag-card { border-radius: 8px; padding: 0.8rem 1rem; margin-bottom: 0.5rem; font-size: 0.88rem; }
.flag-red { background: #fff5f5; border-left: 4px solid #e53e3e; color: #742a2a; }
.flag-green { background: #f0fff4; border-left: 4px solid #38a169; color: #22543d; }
.flag-yellow { background: #fffff0; border-left: 4px solid #d69e2e; color: #744210; }
.thesis-card { background: #ebf8ff; border-left: 4px solid #3182ce; border-radius: 8px; padding: 0.8rem 1rem; margin-bottom: 0.6rem; font-size: 0.9rem; color: #2c5282; }
.rec-buy { background: #c6f6d5; color: #22543d; padding: 6px 16px; border-radius: 20px; font-weight: 700; font-size: 0.9rem; }
.rec-hold { background: #fefcbf; color: #744210; padding: 6px 16px; border-radius: 20px; font-weight: 700; font-size: 0.9rem; }
.rec-sell { background: #fed7d7; color: #742a2a; padding: 6px 16px; border-radius: 20px; font-weight: 700; font-size: 0.9rem; }
</style>
""", unsafe_allow_html=True)

# ── SIDEBAR ──────────────────────────────────────────────
with st.sidebar:
    st.markdown("### 📊 BCTC Analyzer Pro")
    st.markdown("---")
    st.markdown("**Bước 1:** Dùng prompt chuẩn với Claude để phân tích PDF BCTC")
    st.markdown("**Bước 2:** Copy JSON output từ Claude")
    st.markdown("**Bước 3:** Paste vào ô bên dưới")
    st.markdown("---")

    json_input = st.text_area(
        "📋 Paste JSON từ Claude vào đây:",
        height=200,
        placeholder='{\n  "metadata": {...},\n  "income_statement": {...},\n  ...\n}',
        key="json_input"
    )

    load_sample = st.button("📂 Load dữ liệu mẫu (Demo)", use_container_width=True)
    analyze_btn = st.button("🚀 Phân tích", type="primary", use_container_width=True)

    st.markdown("---")
    st.caption("Powered by Claude AI · CFA Framework")
    st.caption("v2.0 · Vietnam Market")

# ── LOAD DATA ─────────────────────────────────────────────
data = None

if load_sample:
    from utils.sample_data import get_sample_data
    data = get_sample_data()
    st.session_state["bctc_data"] = data

if analyze_btn and json_input.strip():
    try:
        clean = json_input.strip()
        if clean.startswith("```"):
            clean = clean.split("```")[1]
            if clean.startswith("json"):
                clean = clean[4:]
        data = json.loads(clean)
        st.session_state["bctc_data"] = data
        st.sidebar.success("✅ JSON hợp lệ!")
    except Exception as e:
        st.sidebar.error(f"❌ JSON lỗi: {e}")

if "bctc_data" in st.session_state:
    data = st.session_state["bctc_data"]

# ── MAIN CONTENT ──────────────────────────────────────────
if not data:
    st.markdown("""
    <div class="main-header">
        <h1>📊 BCTC Analyzer Pro — CFA Framework</h1>
        <p>Upload PDF BCTC → Claude phân tích → Paste JSON → Dashboard tự động render</p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
        <div class="metric-card">
            <div style="font-size:2rem">📄</div>
            <div class="metric-lbl" style="font-size:0.9rem;margin-top:8px">Bước 1</div>
            <div style="font-size:0.85rem;color:#4a5568;margin-top:6px">
                Dùng <b>PROMPT_CHUAN.txt</b><br>đính kèm PDF BCTC<br>gửi cho Claude
            </div>
        </div>""", unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="metric-card">
            <div style="font-size:2rem">🤖</div>
            <div class="metric-lbl" style="font-size:0.9rem;margin-top:8px">Bước 2</div>
            <div style="font-size:0.85rem;color:#4a5568;margin-top:6px">
                Claude tự đọc, extract<br>số liệu & phân tích<br>trả về JSON chuẩn
            </div>
        </div>""", unsafe_allow_html=True)
    with col3:
        st.markdown("""
        <div class="metric-card">
            <div style="font-size:2rem">📊</div>
            <div class="metric-lbl" style="font-size:0.9rem;margin-top:8px">Bước 3</div>
            <div style="font-size:0.85rem;color:#4a5568;margin-top:6px">
                Paste JSON vào sidebar<br>→ Dashboard render<br>tự động hoàn chỉnh
            </div>
        </div>""", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.info("👈 Paste JSON vào sidebar hoặc click **Load dữ liệu mẫu** để xem demo")
    st.stop()

# ── PARSE DATA ────────────────────────────────────────────
meta = data.get("metadata", {})
IS = data.get("income_statement", {})
BS = data.get("balance_sheet", {})
CF = data.get("cash_flow", {})
ratios = data.get("calculated_ratios", {})
cfa = data.get("cfa_analysis", {})
valuation = data.get("valuation", {})
quality = data.get("quality_score", {})
altman = data.get("altman_z_score", {})
beneish = data.get("beneish_m_score", {})
projections = data.get("projections", {})
years = meta.get("years", list(IS.keys()))
unit = meta.get("unit", "triệu đồng")

# ── HEADER ────────────────────────────────────────────────
rec = valuation.get("recommendation", "")
rec_badge = ""
if "Buy" in rec or "MUA" in rec:
    rec_badge = f'<span class="rec-buy">▲ {rec}</span>'
elif "Hold" in rec or "Neutral" in rec:
    rec_badge = f'<span class="rec-hold">◆ {rec}</span>'
else:
    rec_badge = f'<span class="rec-sell">▼ {rec}</span>'

st.markdown(f"""
<div class="main-header">
    <h1>📊 {meta.get('company_name','—')} ({meta.get('ticker','—')}) {rec_badge}</h1>
    <p>{meta.get('exchange','')} · {meta.get('industry','')} / {meta.get('sub_industry','')} · Đơn vị: {unit} · Báo cáo: {meta.get('report_type','')}</p>
</div>
""", unsafe_allow_html=True)

# ── TABS ─────────────────────────────────────────────────
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "📈 Tổng quan & BCTC",
    "🔬 Chỉ số CFA",
    "🏆 Chất lượng & Flags",
    "🔮 Định giá & DCF",
    "📊 Dự phóng",
    "⚖️ Altman & Beneish"
])

# ════════════════════════════════════════════════════════
# TAB 1 — TỔNG QUAN & BCTC
# ════════════════════════════════════════════════════════
with tab1:
    # Key metrics
    latest_y = years[-1] if years else None
    prev_y = years[-2] if len(years) > 1 else None

    if latest_y and IS.get(latest_y):
        is_l = IS[latest_y]
        is_p = IS.get(prev_y, {}) if prev_y else {}

        def pct_chg(curr, prev):
            if curr and prev and prev != 0:
                return (curr - prev) / abs(prev) * 100
            return None

        rev_chg = pct_chg(is_l.get("revenue"), is_p.get("revenue"))
        ni_chg = pct_chg(is_l.get("net_income"), is_p.get("net_income"))
        ebitda_chg = pct_chg(is_l.get("ebitda"), is_p.get("ebitda"))

        cols = st.columns(5)
        kpis = [
            ("Doanh thu", is_l.get("revenue", 0), rev_chg, "triệu đ"),
            ("EBITDA", is_l.get("ebitda", 0), ebitda_chg, "triệu đ"),
            ("Lợi nhuận ròng", is_l.get("net_income", 0), ni_chg, "triệu đ"),
            ("Tổng tài sản", BS.get(latest_y, {}).get("total_assets", 0), None, "triệu đ"),
            ("EPS", is_l.get("eps", 0), None, "đ"),
        ]
        for col, (lbl, val, chg, sfx) in zip(cols, kpis):
            with col:
                val_str = f"{val:,.0f}" if val else "N/A"
                chg_html = ""
                if chg is not None:
                    cls = "metric-chg-pos" if chg >= 0 else "metric-chg-neg"
                    arrow = "▲" if chg >= 0 else "▼"
                    chg_html = f'<div class="{cls}">{arrow} {abs(chg):.1f}% YoY</div>'
                st.markdown(f"""
                <div class="metric-card">
                    <div class="metric-val">{val_str}</div>
                    <div class="metric-lbl">{lbl} ({latest_y})</div>
                    {chg_html}
                </div>""", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Revenue & Net Income trend
    col_l, col_r = st.columns(2)
    with col_l:
        st.markdown('<div class="section-header">Xu hướng Doanh thu & Lợi nhuận</div>', unsafe_allow_html=True)
        rev_data = [IS.get(y, {}).get("revenue", 0) / 1000 for y in years]
        ni_data = [IS.get(y, {}).get("net_income", 0) / 1000 for y in years]
        ebitda_data = [IS.get(y, {}).get("ebitda", 0) / 1000 for y in years]

        fig = go.Figure()
        fig.add_trace(go.Bar(x=years, y=rev_data, name="Doanh thu (tỷ)",
                            marker_color="rgba(49,130,206,0.7)",
                            text=[f"{v:.0f}" for v in rev_data], textposition="outside"))
        fig.add_trace(go.Scatter(x=years, y=ebitda_data, name="EBITDA (tỷ)",
                                mode="lines+markers", line=dict(color="#d69e2e", width=2.5),
                                yaxis="y2"))
        fig.add_trace(go.Scatter(x=years, y=ni_data, name="LNST (tỷ)",
                                mode="lines+markers", line=dict(color="#38a169", width=2.5),
                                yaxis="y2"))
        fig.update_layout(
            height=300, barmode="overlay",
            yaxis=dict(title="Doanh thu (tỷ đ)"),
            yaxis2=dict(title="Lợi nhuận (tỷ đ)", overlaying="y", side="right"),
            legend=dict(orientation="h", y=1.08),
            margin=dict(l=0, r=0, t=10, b=0),
            plot_bgcolor="white", paper_bgcolor="white",
        )
        st.plotly_chart(fig, use_container_width=True)

    with col_r:
        st.markdown('<div class="section-header">Xu hướng Margin (%)</div>', unsafe_allow_html=True)
        gm = [ratios.get(y, {}).get("gross_margin", 0) for y in years]
        ebitdam = [ratios.get(y, {}).get("ebitda_margin", 0) for y in years]
        nm = [ratios.get(y, {}).get("net_margin", 0) for y in years]

        fig2 = go.Figure()
        fig2.add_trace(go.Scatter(x=years, y=gm, name="Gross Margin",
                                 mode="lines+markers+text", line=dict(color="#3182ce", width=2),
                                 text=[f"{v:.1f}%" for v in gm], textposition="top center"))
        fig2.add_trace(go.Scatter(x=years, y=ebitdam, name="EBITDA Margin",
                                 mode="lines+markers+text", line=dict(color="#d69e2e", width=2),
                                 text=[f"{v:.1f}%" for v in ebitdam], textposition="top center"))
        fig2.add_trace(go.Scatter(x=years, y=nm, name="Net Margin",
                                 mode="lines+markers+text", line=dict(color="#38a169", width=2),
                                 text=[f"{v:.1f}%" for v in nm], textposition="bottom center"))
        fig2.update_layout(
            height=300, yaxis=dict(ticksuffix="%"),
            legend=dict(orientation="h", y=1.08),
            margin=dict(l=0, r=0, t=10, b=0),
            plot_bgcolor="white", paper_bgcolor="white",
        )
        st.plotly_chart(fig2, use_container_width=True)

    # BCTC Tables
    st.markdown('<div class="section-header">Kết quả kinh doanh (Income Statement)</div>', unsafe_allow_html=True)
    is_rows = {
        "Doanh thu thuần": "revenue", "Giá vốn hàng bán": "cogs",
        "Lợi nhuận gộp": "gross_profit", "Chi phí bán hàng": "selling_expenses",
        "Chi phí quản lý": "admin_expenses", "Lợi nhuận từ HĐKD": "operating_profit",
        "Thu nhập tài chính": "financial_income", "Chi phí tài chính": "financial_expenses",
        "Chi phí lãi vay": "interest_expense", "EBITDA": "ebitda",
        "EBT": "ebt", "Lợi nhuận ròng": "net_income", "EPS (đ)": "eps"
    }
    is_df = {}
    for lbl, key in is_rows.items():
        row = {}
        for y in years:
            val = IS.get(y, {}).get(key, 0)
            if key == "eps":
                row[y] = f"{val:,.0f}" if val else "—"
            else:
                row[y] = f"{val:,.0f}" if val else "—"
        is_df[lbl] = row
    st.dataframe(pd.DataFrame(is_df).T, use_container_width=True)

    # Balance Sheet summary
    col_bs1, col_bs2 = st.columns(2)
    with col_bs1:
        st.markdown('<div class="section-header">Bảng cân đối kế toán</div>', unsafe_allow_html=True)
        bs_rows = {
            "Tiền & tương đương": "cash", "Phải thu ngắn hạn": "accounts_receivable",
            "Hàng tồn kho": "inventory", "Tổng TSNH": "total_current_assets",
            "TSCĐ (net)": "fixed_assets_net", "Tổng TSDH": "total_long_term_assets",
            "TỔNG TÀI SẢN": "total_assets", "Vay NH": "short_term_debt",
            "Tổng nợ NH": "total_current_liabilities", "Vay DH": "long_term_debt",
            "Tổng nợ phải trả": "total_liabilities", "Vốn CSH": "total_equity"
        }
        bs_df = {lbl: {y: f"{BS.get(y, {}).get(key, 0):,.0f}" for y in years} for lbl, key in bs_rows.items()}
        st.dataframe(pd.DataFrame(bs_df).T, use_container_width=True)

    with col_bs2:
        st.markdown('<div class="section-header">Lưu chuyển tiền tệ</div>', unsafe_allow_html=True)
        cf_rows = {
            "CFO (từ HĐKD)": "cfo", "CapEx": "capex", "FCF": "fcf",
            "CFI (đầu tư)": "cfi", "CFF (tài chính)": "cff",
            "Tiền tăng/giảm ròng": "net_cash_change", "Tiền cuối kỳ": "ending_cash"
        }
        cf_df = {lbl: {y: f"{CF.get(y, {}).get(key, 0):,.0f}" for y in years} for lbl, key in cf_rows.items()}
        st.dataframe(pd.DataFrame(cf_df).T, use_container_width=True)

        # CFO vs Net Income chart
        cfo_vals = [CF.get(y, {}).get("cfo", 0) / 1000 for y in years]
        ni_vals = [IS.get(y, {}).get("net_income", 0) / 1000 for y in years]
        fcf_vals = [CF.get(y, {}).get("fcf", 0) / 1000 for y in years]
        fig_cf = go.Figure()
        fig_cf.add_trace(go.Bar(x=years, y=cfo_vals, name="CFO", marker_color="#48bb78", opacity=0.8))
        fig_cf.add_trace(go.Bar(x=years, y=ni_vals, name="LNST", marker_color="#667eea", opacity=0.8))
        fig_cf.add_trace(go.Scatter(x=years, y=fcf_vals, name="FCF", mode="lines+markers",
                                   line=dict(color="#e53e3e", width=2.5)))
        fig_cf.update_layout(barmode="group", height=220,
                             margin=dict(l=0, r=0, t=20, b=0),
                             legend=dict(orientation="h"),
                             plot_bgcolor="white", paper_bgcolor="white")
        st.plotly_chart(fig_cf, use_container_width=True)

# ════════════════════════════════════════════════════════
# TAB 2 — CHỈ SỐ CFA
# ════════════════════════════════════════════════════════
with tab2:
    st.markdown('<div class="section-header">Bộ chỉ số tài chính toàn diện</div>', unsafe_allow_html=True)

    ratio_groups = {
        "📈 Profitability": [
            ("Gross Margin", "gross_margin", "%", True),
            ("EBITDA Margin", "ebitda_margin", "%", True),
            ("EBIT Margin", "ebit_margin", "%", True),
            ("Net Margin", "net_margin", "%", True),
            ("ROE", "roe", "%", True),
            ("ROA", "roa", "%", True),
            ("ROIC", "roic", "%", True),
        ],
        "⚙️ Efficiency": [
            ("Asset Turnover", "asset_turnover", "x", True),
            ("DSO (ngày)", "dso", " ngày", False),
            ("DIO (ngày)", "dio", " ngày", False),
            ("DPO (ngày)", "dpo", " ngày", True),
            ("CCC (ngày)", "ccc", " ngày", False),
        ],
        "💧 Liquidity": [
            ("Current Ratio", "current_ratio", "x", True),
            ("Quick Ratio", "quick_ratio", "x", True),
            ("Cash Ratio", "cash_ratio", "x", True),
        ],
        "🏗️ Leverage": [
            ("Debt/Equity", "debt_to_equity", "x", False),
            ("Debt/Assets", "debt_to_assets", "x", False),
            ("Debt/EBITDA", "debt_to_ebitda", "x", False),
            ("Interest Coverage", "interest_coverage", "x", True),
        ],
        "💵 Cash Quality": [
            ("Cash Conversion", "cash_conversion_ratio", "x", True),
            ("FCF Margin", "fcf_margin", "%", True),
            ("CFO/Debt", "cfo_to_debt", "x", True),
            ("CapEx/Revenue", "capex_to_revenue", "%", False),
        ],
        "🔬 DuPont": [
            ("Net Margin", "dupont_net_margin", "%", True),
            ("Asset Turnover", "dupont_asset_turnover", "x", True),
            ("Financial Leverage", "dupont_leverage", "x", None),
            ("ROE (DuPont)", "dupont_roe", "%", True),
        ],
    }

    for group_name, metrics in ratio_groups.items():
        st.markdown(f"**{group_name}**")
        df_ratio = {}
        for lbl, key, sfx, higher_better in metrics:
            row = {}
            for y in years:
                val = ratios.get(y, {}).get(key, 0)
                row[y] = f"{val:.2f}{sfx}" if val else "—"
            df_ratio[lbl] = row
        st.dataframe(pd.DataFrame(df_ratio).T, use_container_width=True)
        st.markdown("<br>", unsafe_allow_html=True)

    # DuPont chart
    st.markdown('<div class="section-header">DuPont Decomposition</div>', unsafe_allow_html=True)
    dp_roe = [ratios.get(y, {}).get("dupont_roe", 0) for y in years]
    dp_nm = [ratios.get(y, {}).get("dupont_net_margin", 0) for y in years]
    dp_at = [ratios.get(y, {}).get("dupont_asset_turnover", 0) for y in years]
    dp_lev = [ratios.get(y, {}).get("dupont_leverage", 0) for y in years]

    fig_dp = make_subplots(rows=1, cols=3, subplot_titles=("Net Margin %", "Asset Turnover x", "Leverage x"))
    fig_dp.add_trace(go.Bar(x=years, y=dp_nm, marker_color="#48bb78", name="Net Margin"), row=1, col=1)
    fig_dp.add_trace(go.Bar(x=years, y=dp_at, marker_color="#3182ce", name="Turnover"), row=1, col=2)
    fig_dp.add_trace(go.Bar(x=years, y=dp_lev, marker_color="#d69e2e", name="Leverage"), row=1, col=3)
    fig_dp.update_layout(height=250, margin=dict(l=0, r=0, t=30, b=0),
                        showlegend=False, plot_bgcolor="white", paper_bgcolor="white")
    st.plotly_chart(fig_dp, use_container_width=True)
    roe_parts = [f"{y}: {ratios.get(y,{}).get('dupont_roe',0):.1f}%" for y in years]
    st.markdown(f"**ROE tổng hợp:** {' → '.join(roe_parts)}")

# ════════════════════════════════════════════════════════
# TAB 3 — CHẤT LƯỢNG & FLAGS
# ════════════════════════════════════════════════════════
with tab3:
    col_q1, col_q2 = st.columns([1, 1])

    with col_q1:
        st.markdown('<div class="section-header">Quality Score</div>', unsafe_allow_html=True)
        pct = quality.get("percentage", 0)
        grade = quality.get("grade", "N/A")

        fig_gauge = go.Figure(go.Indicator(
            mode="gauge+number",
            value=pct,
            title={"text": f"Điểm chất lượng — Grade {grade}", "font": {"size": 14}},
            number={"suffix": "/100"},
            gauge={
                "axis": {"range": [0, 100]},
                "bar": {"color": "#3182ce"},
                "steps": [
                    {"range": [0, 40], "color": "#fed7d7"},
                    {"range": [40, 70], "color": "#fef3c7"},
                    {"range": [70, 100], "color": "#c6f6d5"},
                ],
            },
        ))
        fig_gauge.update_layout(height=250, margin=dict(l=20, r=20, t=40, b=10))
        st.plotly_chart(fig_gauge, use_container_width=True)

        # Score breakdown
        components = quality.get("components", {})
        if components:
            comp_df = []
            for k, v in components.items():
                comp_df.append({"Tiêu chí": k, "Điểm": v.get("score", 0),
                               "Max": v.get("max", 10), "Giá trị": v.get("value", 0),
                               "Nhận xét": v.get("comment", "")})
            st.dataframe(pd.DataFrame(comp_df).set_index("Tiêu chí"), use_container_width=True)

    with col_q2:
        # Radar chart
        if components:
            labels = list(components.keys())
            vals = [v.get("score", 0) / v.get("max", 10) * 100 for v in components.values()]
            fig_radar = go.Figure(go.Scatterpolar(
                r=vals + [vals[0]], theta=labels + [labels[0]],
                fill="toself", fillcolor="rgba(49,130,206,0.2)",
                line=dict(color="#3182ce", width=2),
            ))
            fig_radar.update_layout(
                polar=dict(radialaxis=dict(range=[0, 100])),
                height=300, margin=dict(l=30, r=30, t=20, b=20),
                showlegend=False,
            )
            st.plotly_chart(fig_radar, use_container_width=True)

    # Investment Thesis
    st.markdown('<div class="section-header">Investment Thesis</div>', unsafe_allow_html=True)
    thesis = cfa.get("investment_thesis", {})
    for k, v in thesis.items():
        if v:
            st.markdown(f'<div class="thesis-card">💡 <b>{k.replace("_"," ").title()}</b>: {v}</div>',
                       unsafe_allow_html=True)

    # Business Quality
    bq = cfa.get("business_quality", {})
    if bq:
        st.markdown('<div class="section-header">Chất lượng mô hình kinh doanh</div>', unsafe_allow_html=True)
        c1, c2, c3, c4 = st.columns(4)
        c1.metric("Moat Type", bq.get("moat_type", "—"))
        c2.metric("Moat Strength", bq.get("moat_strength", "—"))
        c3.metric("Operating Leverage", bq.get("operating_leverage", "—"))
        c4.metric("Capital Intensity", bq.get("capital_intensity", "—"))
        st.caption(f"Mô hình doanh thu: {bq.get('revenue_model','—')}")
        st.caption(f"Cơ cấu chi phí: {bq.get('cost_structure','—')}")

    # Red / Green Flags
    col_r, col_g = st.columns(2)
    with col_r:
        st.markdown('<div class="section-header">🔴 Red Flags</div>', unsafe_allow_html=True)
        red_flags = cfa.get("red_flags", [])
        if red_flags:
            for f in red_flags:
                sev = f.get("severity", "")
                icon = "🔴" if sev == "High" else ("🟡" if sev == "Medium" else "🟠")
                st.markdown(f"""
                <div class="flag-card flag-red">
                    {icon} <b>[{sev}]</b> {f.get('flag','')}<br>
                    <small>📊 {f.get('evidence','')}</small>
                </div>""", unsafe_allow_html=True)
        else:
            st.success("Không có red flag nghiêm trọng")

    with col_g:
        st.markdown('<div class="section-header">✅ Green Flags</div>', unsafe_allow_html=True)
        green_flags = cfa.get("green_flags", [])
        if green_flags:
            for f in green_flags:
                st.markdown(f"""
                <div class="flag-card flag-green">
                    ✅ {f.get('flag','')}<br>
                    <small>📊 {f.get('evidence','')}</small>
                </div>""", unsafe_allow_html=True)
        else:
            st.warning("Chưa có green flag rõ ràng")

    # Overall assessment
    assessment = cfa.get("overall_assessment", "")
    if assessment:
        st.markdown('<div class="section-header">📝 Đánh giá tổng thể</div>', unsafe_allow_html=True)
        st.info(assessment)

# ════════════════════════════════════════════════════════
# TAB 4 — ĐỊNH GIÁ & DCF
# ════════════════════════════════════════════════════════
with tab4:
    dcf = valuation.get("dcf", {})
    multiples = valuation.get("multiples", {})

    col_rec, col_target = st.columns([1, 2])
    with col_rec:
        st.markdown('<div class="section-header">Khuyến nghị</div>', unsafe_allow_html=True)
        rec = valuation.get("recommendation", "—")
        target = valuation.get("consensus_target", 0)
        st.markdown(f"**Khuyến nghị:** {rec_badge}", unsafe_allow_html=True)
        st.metric("Giá mục tiêu consensus", f"{target:,.0f} đ" if target else "—")
        rationale = valuation.get("recommendation_rationale", "")
        if rationale:
            st.caption(rationale)

    with col_target:
        # Bull/Base/Bear comparison
        st.markdown('<div class="section-header">Bull / Base / Bear</div>', unsafe_allow_html=True)
        cases = ["Bear", "Base", "Bull"]
        case_keys = ["bear_case", "base_case", "bull_case"]
        colors_case = ["#e53e3e", "#3182ce", "#38a169"]

        cols_case = st.columns(3)
        for col, case, key, color in zip(cols_case, cases, case_keys, colors_case):
            with col:
                case_data = dcf.get(key, {})
                price = case_data.get("intrinsic_value_per_share", 0)
                upside = case_data.get("upside_downside_pct", 0)
                wacc = case_data.get("wacc", 0)
                g = case_data.get("revenue_growth_y1_y3", 0)
                st.markdown(f"""
                <div class="metric-card">
                    <div class="metric-val" style="color:{color}">{price:,.0f}đ</div>
                    <div class="metric-lbl">{case} Case</div>
                    <div style="font-size:0.85rem;color:{color};font-weight:600">{upside:+.1f}%</div>
                    <div style="font-size:0.75rem;color:#718096">WACC {wacc:.1f}% · g {g:.1f}%</div>
                </div>""", unsafe_allow_html=True)

    # Range chart
    st.markdown('<div class="section-header">Biểu đồ định giá</div>', unsafe_allow_html=True)
    bear_p = dcf.get("bear_case", {}).get("intrinsic_value_per_share", 0)
    base_p = dcf.get("base_case", {}).get("intrinsic_value_per_share", 0)
    bull_p = dcf.get("bull_case", {}).get("intrinsic_value_per_share", 0)
    pe_p = multiples.get("pe_implied_price", 0)
    pb_p = multiples.get("pb_implied_price", 0)
    ev_p = multiples.get("ev_ebitda_implied_price", 0)

    all_prices = [p for p in [bear_p, base_p, bull_p, pe_p, pb_p, ev_p] if p > 0]
    if all_prices:
        methods = []
        prices = []
        method_colors = []
        for name, val, color in [
            ("DCF Bear", bear_p, "#e53e3e"), ("DCF Base", base_p, "#3182ce"),
            ("DCF Bull", bull_p, "#38a169"), ("P/E Implied", pe_p, "#d69e2e"),
            ("P/B Implied", pb_p, "#9f7aea"), ("EV/EBITDA", ev_p, "#ed8936"),
        ]:
            if val > 0:
                methods.append(name)
                prices.append(val)
                method_colors.append(color)

        fig_val = go.Figure()
        fig_val.add_trace(go.Bar(
            x=methods, y=prices,
            marker_color=method_colors,
            text=[f"{p:,.0f}" for p in prices],
            textposition="outside",
        ))
        if target:
            fig_val.add_hline(y=target, line_dash="dash", line_color="#718096",
                             annotation_text=f"Consensus: {target:,.0f}")
        fig_val.update_layout(
            height=320, margin=dict(l=0, r=0, t=20, b=0),
            plot_bgcolor="white", paper_bgcolor="white",
            yaxis=dict(title="Giá (đ)"),
        )
        st.plotly_chart(fig_val, use_container_width=True)

    # DCF Assumptions
    assumptions = dcf.get("assumptions_rationale", "")
    if assumptions:
        st.markdown('<div class="section-header">Giả định DCF</div>', unsafe_allow_html=True)
        st.info(assumptions)

    # Multiples table
    st.markdown('<div class="section-header">Comparable Multiples</div>', unsafe_allow_html=True)
    mult_df = {
        "Peer Avg P/E": multiples.get("peer_avg_pe", "—"),
        "P/E Implied Price": f"{multiples.get('pe_implied_price', 0):,.0f}đ",
        "Peer Avg P/B": multiples.get("peer_avg_pb", "—"),
        "P/B Implied Price": f"{multiples.get('pb_implied_price', 0):,.0f}đ",
        "Peer Avg EV/EBITDA": multiples.get("peer_avg_ev_ebitda", "—"),
        "EV/EBITDA Implied": f"{multiples.get('ev_ebitda_implied_price', 0):,.0f}đ",
        "Peer Companies": ", ".join(multiples.get("peer_companies", [])),
    }
    st.table(pd.DataFrame.from_dict(mult_df, orient="index", columns=["Giá trị"]))

# ════════════════════════════════════════════════════════
# TAB 5 — DỰ PHÓNG
# ════════════════════════════════════════════════════════
with tab5:
    proj_years = [y for y in projections.keys() if y.isdigit()]
    if proj_years:
        st.markdown('<div class="section-header">Dự phóng tài chính 3-5 năm</div>', unsafe_allow_html=True)

        all_years_chart = years + proj_years
        rev_hist = [IS.get(y, {}).get("revenue", 0) / 1000 for y in years]
        rev_proj = [projections.get(y, {}).get("revenue", 0) / 1000 for y in proj_years]
        ni_hist = [IS.get(y, {}).get("net_income", 0) / 1000 for y in years]
        ni_proj = [projections.get(y, {}).get("net_income", 0) / 1000 for y in proj_years]

        fig_proj = go.Figure()
        # Historical
        fig_proj.add_trace(go.Bar(x=years, y=rev_hist, name="Doanh thu thực",
                                 marker_color="rgba(49,130,206,0.8)"))
        # Projected
        fig_proj.add_trace(go.Bar(x=proj_years, y=rev_proj, name="Doanh thu dự phóng",
                                 marker_color="rgba(49,130,206,0.3)",
                                 marker_pattern_shape="x"))
        fig_proj.add_trace(go.Scatter(x=years, y=ni_hist, name="LNST thực",
                                     mode="lines+markers", line=dict(color="#38a169", width=2.5)))
        fig_proj.add_trace(go.Scatter(x=proj_years, y=ni_proj, name="LNST dự phóng",
                                     mode="lines+markers", line=dict(color="#38a169", width=2.5, dash="dot")))
        fig_proj.update_layout(
            height=320, barmode="overlay",
            yaxis=dict(title="Tỷ đồng"),
            legend=dict(orientation="h"),
            margin=dict(l=0, r=0, t=20, b=0),
            plot_bgcolor="white", paper_bgcolor="white",
        )
        # Add separator line between historical and projected
        if years and proj_years:
            fig_proj.add_vline(x=2.5, line_dash="dot", line_color="#a0aec0",
                              annotation_text="← Thực tế | Dự phóng →")
        st.plotly_chart(fig_proj, use_container_width=True)

        # Projection table
        proj_rows = {
            "Doanh thu (tỷ)": "revenue", "EBITDA (tỷ)": "ebitda",
            "LNST (tỷ)": "net_income", "FCF (tỷ)": "fcf", "EPS (đ)": "eps"
        }
        proj_df = {}
        for lbl, key in proj_rows.items():
            row = {}
            for y in proj_years:
                val = projections.get(y, {}).get(key, 0)
                if key == "eps":
                    row[y] = f"{val:,.0f}"
                else:
                    row[y] = f"{val/1000:,.1f}"
            proj_df[lbl] = row
        st.dataframe(pd.DataFrame(proj_df).T, use_container_width=True)

        # Assumptions
        assump = projections.get("assumptions", {})
        if assump:
            st.markdown('<div class="section-header">Giả định dự phóng</div>', unsafe_allow_html=True)
            col_a1, col_a2 = st.columns(2)
            with col_a1:
                st.markdown(f"**Tăng trưởng doanh thu:** {assump.get('revenue_drivers','—')}")
                st.markdown(f"**Margin:** {assump.get('margin_drivers','—')}")
            with col_a2:
                st.markdown(f"**CapEx:** {assump.get('capex_assumption','—')}")
                risks = assump.get("key_risks_to_projections", [])
                if risks:
                    st.markdown("**Rủi ro chính:**")
                    for r in risks:
                        st.markdown(f"⚠️ {r}")
    else:
        st.info("Không có dữ liệu dự phóng. Claude cần được cung cấp thêm context ngành để dự phóng.")

# ════════════════════════════════════════════════════════
# TAB 6 — ALTMAN & BENEISH
# ════════════════════════════════════════════════════════
with tab6:
    col_az, col_bm = st.columns(2)

    with col_az:
        st.markdown('<div class="section-header">Altman Z''-Score</div>', unsafe_allow_html=True)
        z_latest = altman.get(latest_y or "2024", altman.get(list(altman.keys())[-1] if altman else "2024", {}))
        if z_latest:
            z = z_latest.get("z_score", 0)
            zone = z_latest.get("zone", "")
            interp = z_latest.get("interpretation", "")

            fig_z = go.Figure(go.Indicator(
                mode="gauge+number",
                value=z,
                title={"text": f"Z'' = {z:.2f} — {zone}"},
                gauge={
                    "axis": {"range": [0, 5]},
                    "bar": {"color": "#3182ce"},
                    "steps": [
                        {"range": [0, 1.1], "color": "#fed7d7"},
                        {"range": [1.1, 2.6], "color": "#fef3c7"},
                        {"range": [2.6, 5], "color": "#c6f6d5"},
                    ],
                },
            ))
            fig_z.update_layout(height=250, margin=dict(l=20, r=20, t=40, b=10))
            st.plotly_chart(fig_z, use_container_width=True)

            for k in ["x1_working_capital_to_assets", "x2_retained_earnings_to_assets",
                     "x3_ebit_to_assets", "x4_equity_to_liabilities"]:
                val = z_latest.get(k)
                if val is not None:
                    label = k.replace("_", " ").upper()
                    icon = "🟢" if val > 0 else "🔴"
                    st.markdown(f"{icon} **{label}**: `{val:.3f}`")
            if interp:
                st.info(interp)

    with col_bm:
        st.markdown('<div class="section-header">Beneish M-Score</div>', unsafe_allow_html=True)
        for period, b_data in beneish.items():
            if not b_data:
                continue
            m = b_data.get("m_score", 0)
            risk = b_data.get("risk_level", "")
            interp = b_data.get("interpretation", "")

            if m > -1.78:
                st.error(f"🔴 **{period}** — M = {m:.2f} — HIGH RISK")
            elif m > -2.22:
                st.warning(f"🟡 **{period}** — M = {m:.2f} — MEDIUM RISK")
            else:
                st.success(f"🟢 **{period}** — M = {m:.2f} — LOW RISK")

            beneish_vars = ["dsri", "gmi", "aqi", "sgi", "depi", "sgai", "lvgi", "tata"]
            thresholds = {"dsri": 1.465, "gmi": 1.193, "aqi": 1.254, "sgi": 1.607,
                         "depi": 1.082, "sgai": 1.041, "lvgi": 1.0, "tata": 0.031}
            rows = []
            for var in beneish_vars:
                val = b_data.get(var)
                if val is not None:
                    alert = val > thresholds.get(var, 999)
                    rows.append({"Biến": var.upper(), "Giá trị": round(val, 3),
                                "Ngưỡng": thresholds.get(var, "—"),
                                "Status": "🔴 ALERT" if alert else "🟢 OK"})
            if rows:
                st.dataframe(pd.DataFrame(rows).set_index("Biến"), use_container_width=True)
            if interp:
                st.caption(interp)
            st.markdown("---")
