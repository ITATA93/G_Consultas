# SQLUser.PA_LabourNewBornCareReq

**Schema:** SQLUser
**Columnas:** 6
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| IMC_ParRef | varchar | PK |  | NO | PA_LabourNewBorn Parent Reference |
| IMC_Childsub | double |  |  | NO | Childsub |
| IMC_DateFrom | date |  |  | SI | Date From |
| IMC_DateTo | date |  |  | SI | Date To |
| IMC_ImmedCare_DR | bigint |  | FK | SI | Des Ref to ImmedCare |
| IMC_RowId | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*