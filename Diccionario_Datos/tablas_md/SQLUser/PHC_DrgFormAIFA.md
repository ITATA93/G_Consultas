# SQLUser.PHC_DrgFormAIFA

**Schema:** SQLUser
**Columnas:** 16
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Farmacia Clínica**. Validación farmacéutica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| AIFA_ParRef | varchar | PK |  | NO | PHC_DrgForm Parent Reference |
| AIFA_AIFA_DR | bigint |  | FK | SI | Des Ref PHCAIFANotes |
| AIFA_Childsub | double |  |  | NO | Childsub |
| AIFA_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| AIFA_CreatedDate | date |  |  | SI | Created Date |
| AIFA_CreatedTime | time |  |  | SI | Created Time |
| AIFA_CreatedUser_DR | bigint |  | FK | SI | Created User |
| AIFA_DateFrom | date |  |  | SI | Date From |
| AIFA_DateTo | date |  |  | SI | Date To |
| AIFA_HCA_DR | bigint |  | FK | SI | Des Ref HealthCareArea |
| AIFA_HCR_DR | bigint |  | FK | SI | Des Ref HealthCareRegion |
| AIFA_National | varchar |  |  | SI | National  |
| AIFA_RowId | varchar |  |  | NO | - |
| AIFA_UpdatedDate | date |  |  | SI | Updated Date |
| AIFA_UpdatedTime | time |  |  | SI | Updated Time |
| AIFA_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*