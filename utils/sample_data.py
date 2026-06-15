def get_sample_data():
    """Sample data based on a fictional Vietnamese listed company for demo purposes."""
    return {
        "metadata": {
            "company_name": "Công ty CP Sữa Việt Nam (Demo)",
            "ticker": "VNM",
            "exchange": "HOSE",
            "industry": "Hàng tiêu dùng",
            "sub_industry": "Thực phẩm & Đồ uống",
            "report_type": "Kiểm toán",
            "currency": "VND",
            "unit": "triệu đồng",
            "years": ["2022", "2023", "2024"],
            "extraction_notes": "Dữ liệu mẫu để demo — không phải số liệu thực"
        },
        "income_statement": {
            "2022": {"revenue": 60919000, "cogs": 37500000, "gross_profit": 23419000,
                     "selling_expenses": 7200000, "admin_expenses": 1800000, "operating_profit": 14419000,
                     "financial_income": 1200000, "financial_expenses": 180000, "interest_expense": 120000,
                     "other_income": 50000, "ebt": 15489000, "tax": 2400000, "net_income": 9180000,
                     "net_income_parent": 9000000, "minority_interest": 180000,
                     "ebitda": 11500000, "depreciation_amortization": 1200000,
                     "shares_outstanding": 2089955600, "eps": 4300},
            "2023": {"revenue": 58200000, "cogs": 36100000, "gross_profit": 22100000,
                     "selling_expenses": 6900000, "admin_expenses": 1750000, "operating_profit": 13450000,
                     "financial_income": 1350000, "financial_expenses": 160000, "interest_expense": 100000,
                     "other_income": 30000, "ebt": 14670000, "tax": 2200000, "net_income": 8500000,
                     "net_income_parent": 8320000, "minority_interest": 180000,
                     "ebitda": 10800000, "depreciation_amortization": 1250000,
                     "shares_outstanding": 2089955600, "eps": 3980},
            "2024": {"revenue": 62500000, "cogs": 38200000, "gross_profit": 24300000,
                     "selling_expenses": 7100000, "admin_expenses": 1820000, "operating_profit": 15380000,
                     "financial_income": 1500000, "financial_expenses": 150000, "interest_expense": 90000,
                     "other_income": 60000, "ebt": 16790000, "tax": 2520000, "net_income": 10200000,
                     "net_income_parent": 9950000, "minority_interest": 250000,
                     "ebitda": 12800000, "depreciation_amortization": 1350000,
                     "shares_outstanding": 2089955600, "eps": 4760}
        },
        "balance_sheet": {
            "2022": {"cash": 4200000, "short_term_investments": 8500000, "accounts_receivable": 2100000,
                     "inventory": 3800000, "other_current_assets": 800000, "total_current_assets": 19400000,
                     "fixed_assets_net": 9200000, "long_term_investments": 3100000,
                     "other_long_term_assets": 1200000, "total_long_term_assets": 13500000,
                     "total_assets": 32900000, "short_term_debt": 1200000, "accounts_payable": 3100000,
                     "other_current_liabilities": 2800000, "total_current_liabilities": 7100000,
                     "long_term_debt": 500000, "other_long_term_liabilities": 400000,
                     "total_liabilities": 8000000, "charter_capital": 20900000,
                     "retained_earnings": 2500000, "other_equity": 800000,
                     "total_equity_parent": 24100000, "minority_interest_bs": 800000,
                     "total_equity": 24900000},
            "2023": {"cash": 5100000, "short_term_investments": 9200000, "accounts_receivable": 1950000,
                     "inventory": 3500000, "other_current_assets": 750000, "total_current_assets": 20500000,
                     "fixed_assets_net": 8800000, "long_term_investments": 3300000,
                     "other_long_term_assets": 1100000, "total_long_term_assets": 13200000,
                     "total_assets": 33700000, "short_term_debt": 1000000, "accounts_payable": 2900000,
                     "other_current_liabilities": 2600000, "total_current_liabilities": 6500000,
                     "long_term_debt": 400000, "other_long_term_liabilities": 350000,
                     "total_liabilities": 7250000, "charter_capital": 20900000,
                     "retained_earnings": 3800000, "other_equity": 900000,
                     "total_equity_parent": 25650000, "minority_interest_bs": 800000,
                     "total_equity": 26450000},
            "2024": {"cash": 6800000, "short_term_investments": 10500000, "accounts_receivable": 2050000,
                     "inventory": 3650000, "other_current_assets": 820000, "total_current_assets": 23820000,
                     "fixed_assets_net": 9500000, "long_term_investments": 3500000,
                     "other_long_term_assets": 1300000, "total_long_term_assets": 14300000,
                     "total_assets": 38120000, "short_term_debt": 800000, "accounts_payable": 3200000,
                     "other_current_liabilities": 2700000, "total_current_liabilities": 6700000,
                     "long_term_debt": 300000, "other_long_term_liabilities": 380000,
                     "total_liabilities": 7380000, "charter_capital": 20900000,
                     "retained_earnings": 8200000, "other_equity": 850000,
                     "total_equity_parent": 29950000, "minority_interest_bs": 790000,
                     "total_equity": 30740000}
        },
        "cash_flow": {
            "2022": {"cfo": 10800000, "net_income_cf": 9180000, "depreciation_cf": 1200000,
                     "working_capital_change": 420000, "cfi": -2100000, "capex": -1800000,
                     "acquisitions": -300000, "cff": -8500000, "debt_raised": 200000,
                     "debt_repaid": -500000, "dividends_paid": -8200000,
                     "net_cash_change": 200000, "ending_cash": 4200000, "fcf": 9000000},
            "2023": {"cfo": 9500000, "net_income_cf": 8500000, "depreciation_cf": 1250000,
                     "working_capital_change": -250000, "cfi": -1800000, "capex": -1500000,
                     "acquisitions": -300000, "cff": -7600000, "debt_raised": 100000,
                     "debt_repaid": -400000, "dividends_paid": -7300000,
                     "net_cash_change": 100000, "ending_cash": 5100000, "fcf": 8000000},
            "2024": {"cfo": 12200000, "net_income_cf": 10200000, "depreciation_cf": 1350000,
                     "working_capital_change": 650000, "cfi": -2500000, "capex": -2100000,
                     "acquisitions": -400000, "cff": -9000000, "debt_raised": 150000,
                     "debt_repaid": -550000, "dividends_paid": -8600000,
                     "net_cash_change": 700000, "ending_cash": 6800000, "fcf": 10100000}
        },
        "calculated_ratios": {
            "2022": {"gross_margin": 38.4, "ebitda_margin": 18.9, "ebit_margin": 16.8,
                     "net_margin": 15.1, "roe": 36.9, "roa": 27.9, "roic": 32.1,
                     "asset_turnover": 1.85, "inventory_turnover": 9.9, "receivable_turnover": 29.0,
                     "dso": 12.6, "dio": 37.0, "dpo": 30.1, "ccc": 19.5,
                     "current_ratio": 2.73, "quick_ratio": 2.2, "cash_ratio": 0.59,
                     "debt_to_equity": 0.07, "debt_to_assets": 0.05, "net_debt": -11000000,
                     "debt_to_ebitda": 0.15, "interest_coverage": 95.8,
                     "cash_conversion_ratio": 1.18, "capex_to_revenue": 2.95,
                     "fcf_margin": 14.8, "cfo_to_debt": 6.4,
                     "dupont_net_margin": 15.1, "dupont_asset_turnover": 1.85, "dupont_leverage": 1.32, "dupont_roe": 36.9},
            "2023": {"gross_margin": 38.0, "ebitda_margin": 18.6, "ebit_margin": 16.5,
                     "net_margin": 14.6, "roe": 32.1, "roa": 25.2, "roic": 29.8,
                     "asset_turnover": 1.73, "inventory_turnover": 10.3, "receivable_turnover": 29.8,
                     "dso": 12.2, "dio": 35.4, "dpo": 29.3, "ccc": 18.3,
                     "current_ratio": 3.15, "quick_ratio": 2.6, "cash_ratio": 0.78,
                     "debt_to_equity": 0.05, "debt_to_assets": 0.04, "net_debt": -12900000,
                     "debt_to_ebitda": 0.13, "interest_coverage": 108.0,
                     "cash_conversion_ratio": 1.12, "capex_to_revenue": 2.58,
                     "fcf_margin": 13.7, "cfo_to_debt": 6.8,
                     "dupont_net_margin": 14.6, "dupont_asset_turnover": 1.73, "dupont_leverage": 1.27, "dupont_roe": 32.1},
            "2024": {"gross_margin": 38.9, "ebitda_margin": 20.5, "ebit_margin": 18.2,
                     "net_margin": 16.3, "roe": 33.2, "roa": 26.8, "roic": 31.5,
                     "asset_turnover": 1.64, "inventory_turnover": 10.5, "receivable_turnover": 30.5,
                     "dso": 12.0, "dio": 34.8, "dpo": 30.6, "ccc": 16.2,
                     "current_ratio": 3.55, "quick_ratio": 3.0, "cash_ratio": 1.01,
                     "debt_to_equity": 0.04, "debt_to_assets": 0.03, "net_debt": -16500000,
                     "debt_to_ebitda": 0.09, "interest_coverage": 142.2,
                     "cash_conversion_ratio": 1.20, "capex_to_revenue": 3.36,
                     "fcf_margin": 16.2, "cfo_to_debt": 10.9,
                     "dupont_net_margin": 16.3, "dupont_asset_turnover": 1.64, "dupont_leverage": 1.24, "dupont_roe": 33.2}
        },
        "altman_z_score": {
            "2024": {"x1_working_capital_to_assets": 0.449, "x2_retained_earnings_to_assets": 0.215,
                     "x3_ebit_to_assets": 0.404, "x4_equity_to_liabilities": 4.165,
                     "z_score": 4.82, "zone": "Safe Zone 🟢",
                     "interpretation": "Z'' = 4.82 vượt ngưỡng Safe Zone (>2.6). Doanh nghiệp có sức khỏe tài chính rất tốt, rủi ro phá sản cực thấp. Đặc biệt X4 (Equity/Liabilities = 4.17x) phản ánh cấu trúc vốn bảo thủ, ít nợ."}
        },
        "beneish_m_score": {
            "2023_vs_2022": {"dsri": 0.95, "gmi": 1.01, "aqi": 0.98, "sgi": 0.955,
                            "depi": 1.04, "sgai": 0.98, "lvgi": 0.91, "tata": -0.008,
                            "m_score": -2.85, "risk_level": "Low",
                            "interpretation": "M-Score = -2.85, thấp hơn ngưỡng -2.22. Không có dấu hiệu thao túng BCTC. DSRI < 1 cho thấy phải thu tăng chậm hơn doanh thu — tín hiệu tích cực về chất lượng doanh thu."},
            "2024_vs_2023": {"dsri": 1.02, "gmi": 0.97, "aqi": 1.01, "sgi": 1.074,
                            "depi": 1.02, "sgai": 0.99, "lvgi": 0.88, "tata": 0.004,
                            "m_score": -2.71, "risk_level": "Low",
                            "interpretation": "M-Score = -2.71, vẫn trong ngưỡng Low Risk. SGI = 1.07 phản ánh tăng trưởng doanh thu lành mạnh. Không có biến số nào vượt ngưỡng cảnh báo."}
        },
        "quality_score": {
            "overall_score": 72, "max_score": 80, "percentage": 90, "grade": "A",
            "components": {
                "roe": {"score": 10, "max": 10, "value": 33.2, "comment": "ROE 33.2% vượt xa ngưỡng 15% — chất lượng cao"},
                "net_margin": {"score": 10, "max": 10, "value": 16.3, "comment": "Net Margin 16.3% xuất sắc cho ngành FMCG"},
                "ebitda_margin": {"score": 10, "max": 10, "value": 20.5, "comment": "EBITDA Margin 20.5% > 20% threshold"},
                "interest_coverage": {"score": 10, "max": 10, "value": 142.2, "comment": "ICR = 142x — gần như zero financial risk"},
                "current_ratio": {"score": 10, "max": 10, "value": 3.55, "comment": "Thanh khoản rất tốt, CR = 3.55x"},
                "cash_conversion": {"score": 10, "max": 10, "value": 1.20, "comment": "CCR = 1.20 — lợi nhuận chuyển thành tiền hiệu quả"},
                "debt_ebitda": {"score": 10, "max": 10, "value": 0.09, "comment": "Net cash position — gần như không có nợ"},
                "cfo_debt": {"score": 2, "max": 10, "value": 10.9, "comment": "CFO/Debt = 10.9x — vượt xa mọi ngưỡng"}
            }
        },
        "cfa_analysis": {
            "investment_thesis": {
                "thesis_1": "Market leader không thể thay thế: Chiếm 55%+ thị phần sữa VN với thương hiệu 45 năm, chi phí chuyển đổi cao và mạng lưới phân phối 220,000 điểm bán — tạo moat bền vững khó bị xâm phạm",
                "thesis_2": "Margin expansion cycle: Giá nguyên liệu đầu vào (sữa bột nhập khẩu) giảm 15-20% từ đỉnh 2022, trong khi pricing power cho phép duy trì giá bán → EBITDA margin mở rộng từ 18.6% lên 20.5%+",
                "thesis_3": "Thị trường định giá sai tiềm năng Premium: Phân khúc sữa premium/organic tăng 25% CAGR, VNM đang mở rộng mạnh vào phân khúc này nhưng thị trường chưa price in đầy đủ — reverse DCF cho thấy giá hiện tại price in chỉ 5% growth vs khả năng thực là 8-10%"
            },
            "business_quality": {
                "moat_type": "Brand + Scale + Distribution",
                "moat_strength": "Strong",
                "moat_description": "Thương hiệu 45 năm với NPS cao nhất ngành. Mạng lưới lạnh 220,000 điểm bán độc quyền. Chi phí xây dựng mạng lưới tương tự ước tính >5,000 tỷ đồng — rào cản gia nhập rất cao.",
                "revenue_model": "B2C trực tiếp qua siêu thị/tạp hóa (70%) + B2B qua trường học/bệnh viện (20%) + Export (10%). Recurring demand cao vì sản phẩm thiết yếu.",
                "cost_structure": "variable_heavy",
                "operating_leverage": "Medium",
                "capital_intensity": "Moderate"
            },
            "growth_analysis": {
                "revenue_cagr_3y": 1.3,
                "net_income_cagr_3y": 5.4,
                "growth_quality": "Organic",
                "growth_drivers": ["Tăng trưởng premium segment", "Mở rộng thị phần miền Bắc", "Export tăng trưởng 2 chữ số", "Premiumization pricing"],
                "growth_risks": ["Cạnh tranh từ TH True Milk và Vinamilk quốc tế", "Biến động giá nguyên liệu nhập khẩu", "Thị trường sữa bão hòa tại đô thị lớn"]
            },
            "earnings_quality": {
                "assessment": "High",
                "cash_conversion_trend": "Improving",
                "accruals_ratio": -0.008,
                "revenue_recognition_risk": "Low",
                "key_concerns": ["Working capital management cần cải thiện tại phân khúc export"]
            },
            "red_flags": [
                {"severity": "Low", "flag": "Doanh thu tăng trưởng chậm 3 năm gần nhất", "evidence": "Revenue CAGR 2022-2024 chỉ 1.3% — thị trường nội địa đang bão hòa"}
            ],
            "green_flags": [
                {"flag": "Net cash position mạnh — Net Debt âm 16,500 tỷ đồng", "evidence": "Cash + STI = 17,300 tỷ vs Total Debt = 1,100 tỷ → Net Cash 16,200 tỷ"},
                {"flag": "EBITDA Margin mở rộng liên tục", "evidence": "18.9% (2022) → 18.6% (2023) → 20.5% (2024) — chu kỳ margin expansion đang diễn ra"},
                {"flag": "Cash Conversion Ratio > 1.0 liên tiếp 3 năm", "evidence": "CCR = 1.18 / 1.12 / 1.20 — lợi nhuận chuyển thành tiền thực hiệu quả, rủi ro accounting manipulation thấp"},
                {"flag": "Cổ tức ổn định, dividend yield hấp dẫn", "evidence": "Trả cổ tức 8,200-8,600 tỷ/năm, yield ~5-6% tại mức giá hiện tại"}
            ],
            "overall_assessment": "VNM là doanh nghiệp chất lượng cao với moat bền vững, cấu trúc tài chính xuất sắc (net cash 16,500 tỷ, interest coverage 142x) và margin đang trong chu kỳ mở rộng. Rủi ro chính là tăng trưởng topline chậm do thị trường nội địa bão hòa. Tuy nhiên, với P/E forward ~15x, định giá đang ở vùng hấp dẫn so với chất lượng kinh doanh. Khuyến nghị MUA với horizon 12 tháng."
        },
        "valuation": {
            "dcf": {
                "base_case": {"wacc": 12.0, "terminal_growth": 3.0, "revenue_growth_y1_y3": 8.0,
                             "revenue_growth_y4_y5": 5.0, "ebitda_margin_projection": 21.0,
                             "intrinsic_value_per_share": 95000, "upside_downside_pct": 18.75},
                "bull_case": {"wacc": 11.0, "terminal_growth": 3.5, "revenue_growth_y1_y3": 12.0,
                             "revenue_growth_y4_y5": 7.0, "ebitda_margin_projection": 23.0,
                             "intrinsic_value_per_share": 118000, "upside_downside_pct": 47.5},
                "bear_case": {"wacc": 13.5, "terminal_growth": 2.0, "revenue_growth_y1_y3": 4.0,
                             "revenue_growth_y4_y5": 3.0, "ebitda_margin_projection": 19.0,
                             "intrinsic_value_per_share": 72000, "upside_downside_pct": -10.0},
                "assumptions_rationale": "WACC base case 12% = Risk-free 6.5% + ERP 8% × Beta 0.7 + Size premium 0. Terminal growth 3% phù hợp tăng trưởng dài hạn ngành FMCG VN. Revenue growth 8% dựa trên: premiumization +5%, export +15%, organic +3%. EBITDA margin 21% sau khi normalize giá nguyên liệu."
            },
            "multiples": {
                "pe_implied_price": 88500, "pb_implied_price": 82000, "ev_ebitda_implied_price": 91000,
                "peer_avg_pe": 18.5, "peer_avg_pb": 3.2, "peer_avg_ev_ebitda": 12.5,
                "peer_companies": ["MCM", "IDP", "GTN", "Masan Consumer", "Kido Group"]
            },
            "consensus_target": 92000,
            "recommendation": "Buy",
            "recommendation_rationale": "P/E forward 15x thấp hơn peer average 18.5x với chất lượng kinh doanh vượt trội. DCF base case cho upside 18.75%. Margin expansion cycle chưa được định giá đầy đủ. Cổ tức yield 5-6% cung cấp downside protection."
        },
        "projections": {
            "2025": {"revenue": 67500000, "ebitda": 14200000, "net_income": 11500000, "fcf": 11200000, "eps": 5350},
            "2026": {"revenue": 72900000, "ebitda": 15700000, "net_income": 12800000, "fcf": 12400000, "eps": 5950},
            "2027": {"revenue": 78700000, "ebitda": 17000000, "net_income": 14000000, "fcf": 13500000, "eps": 6510},
            "2028": {"revenue": 82600000, "ebitda": 17900000, "net_income": 14800000, "fcf": 14200000, "eps": 6880},
            "2029": {"revenue": 86700000, "ebitda": 18800000, "net_income": 15600000, "fcf": 15000000, "eps": 7250},
            "assumptions": {
                "revenue_drivers": "2025-2027: 8% CAGR driven by premium segment (25% growth), export expansion (15% growth), organic domestic +3-4%. 2028-2029: normalize to 5% as market matures.",
                "margin_drivers": "EBITDA margin target 21% by 2025 → 22% by 2027 driven by: (1) input cost normalization, (2) premium mix shift, (3) operating leverage từ capacity utilization cao hơn.",
                "capex_assumption": "Maintenance CapEx ~1,500-1,800 tỷ/năm. Growth CapEx thêm 500-800 tỷ cho expansion nhà máy miền Bắc và dây chuyền organic.",
                "key_risks_to_projections": [
                    "Giá sữa bột thế giới tăng mạnh trở lại do El Nino tại Úc/New Zealand",
                    "Cạnh tranh từ các brand premium nước ngoài (Ensure, Similac) tăng tốc",
                    "Tỷ lệ sinh giảm ảnh hưởng dài hạn đến thị trường sữa trẻ em"
                ]
            }
        }
    }
