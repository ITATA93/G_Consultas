# SQLUser.OE_AdmixManufIngrAllocation

**Schema:** SQLUser
**Columnas:** 21
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| AMIA_ParRef | varchar | PK |  | NO | OE_AdmixManufIngr Parent Reference |
| AMIA_AdmixAdditiveAllocation_DR | varchar |  | FK | SI | Des Ref OEAdmix |
| AMIA_Childsub | double |  |  | NO | Childsub |
| AMIA_ExtStkBatchID | varchar |  |  | SI | External Stock BatchID |
| AMIA_ExtStkDetails | varchar |  |  | SI | External Stock Details |
| AMIA_INCIRN_DR | varchar |  | FK | SI | Des Ref INCItmRegNo |
| AMIA_INCLB_DR | varchar |  | FK | SI | Des Ref INCItmLcBt |
| AMIA_Quantity | double |  |  | SI | Quantity |
| AMIA_RowId | varchar |  |  | NO | - |
| ChildQ06DR | - |  |  | SI | Child Reference: Treatment |
| Q05Q1 | - |  |  | SI | Date |
| Q05Q10 | - |  |  | SI | Skin colour surrounding wound |
| Q05Q11 | - |  |  | SI | Granulation tissue |
| Q05Q15 | - |  |  | SI | Note |
| Q05Q2 | - |  |  | SI | Size (length, width and depth) |
| Q05Q3 | - |  |  | SI | Stage of pressure injury |
| Q05Q4 | - |  |  | SI | Edges |
| Q05Q5 | - |  |  | SI | Undermining |
| Q05Q6 | - |  |  | SI | Exudate |
| Q05Q6a | - |  |  | SI | Wound infection |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*