# SQLUser.PA_PersonToothHistory

**Schema:** SQLUser
**Columnas:** 10
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Histórico de cambios.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| HIST_ParRef | varchar | PK |  | NO | PA_PersonTooth Parent Reference |
| HIST_Childsub | double |  |  | NO | Childsub |
| HIST_DentalState_DR | bigint |  | FK | SI | Des Ref DentalState_DR |
| HIST_LastUpdateDate | date |  |  | SI | LastUpdateDate |
| HIST_LastUpdateHospital_DR | bigint |  | FK | SI | Des Ref LastUpdateHospital_DR |
| HIST_LastUpdateTime | time |  |  | SI | LastUpdateTime |
| HIST_LastUpdateUser_DR | bigint |  | FK | SI | Des Ref LastUpdateUser_DR |
| HIST_OEOrdItem_DR | varchar |  | FK | SI | OEOrdItem_DR |
| HIST_RowId | varchar |  |  | NO | - |
| HIST_ToothArea_DR | bigint |  | FK | SI | DR OEc_ToothArea |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*