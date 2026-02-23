# lab.CT_TestCodeStandardComm

**Schema:** lab
**Columnas:** 16
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTTCT_ParRef | varchar | PK |  | NO | CT_TestCode Parent Reference |
| CTTCT_ActiveFlag | varchar |  |  | SI | Active Flag |
| CTTCT_Activity_DR | varchar |  | FK | SI | Activity DR |
| CTTCT_BillingItem_DR | varchar |  | FK | SI | Billing Item DR |
| CTTCT_CancerCouncilCodes | varchar |  |  | SI | Cancer Council Codes |
| CTTCT_Code | varchar |  |  | NO | Code |
| CTTCT_CumPrint | varchar |  |  | SI | Print in Cum reports |
| CTTCT_Flag | varchar |  |  | SI | Flag |
| CTTCT_FontBold | varchar |  |  | SI | Font Bold |
| CTTCT_FontItalic | varchar |  |  | SI | Font Italic |
| CTTCT_FontUnderline | varchar |  |  | SI | Font Underline |
| CTTCT_Formatted | varchar |  |  | SI | Formatted |
| CTTCT_RowId | varchar |  |  | NO | - |
| CTTCT_SNOMEDCodes | varchar |  |  | SI | SNOMED Codes |
| CTTCT_Summary | varchar |  |  | SI | Summary |
| CTTCT_Text | varchar |  |  | SI | Text |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*