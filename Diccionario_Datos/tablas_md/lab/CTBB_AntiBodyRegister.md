# lab.CTBB_AntiBodyRegister

**Schema:** lab
**Columnas:** 7
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo Banco de Sangre**. Configuración de hemoterapia.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| BBAR_RowID | varchar | PK |  | NO | - |
| BBAR_PositiveResult | varchar |  |  | SI | Positive Result |
| BBAR_ResultTestItem_DR | varchar |  | FK | SI | Result TestItem DR |
| BBAR_TestItem_Comment_DR | varchar |  | FK | SI | Test Item Comment DR |
| BBAR_TestItem_Result_DR | varchar |  | FK | NO | Test Item Result DR |
| BBAR_TestSet_DR | varchar |  | FK | NO | Test Set DR |
| BBAR_Type | varchar |  |  | NO | Type |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*