# SQLUser.RVI_InsCoBillTreatmentDays

**Schema:** SQLUser
**Columnas:** 4
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| TDAY_ParRef | bigint | PK |  | NO | RVI_InsCompanyBill Parent Reference |
| TDAY_Childsub | double |  |  | NO | Childsub |
| TDAY_RowId | varchar |  |  | NO | - |
| TDAY_TreatmentDate | double |  |  | SI | Treatment Date |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*