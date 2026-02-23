# SQLUser.PAC_ServiceAgreementSpecialty

**Schema:** SQLUser
**Columnas:** 22
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SPEC_ParRef | bigint | PK |  | NO | PAC_ServiceAgreement Parent Reference |
| Q06Q1 | - |  |  | SI | Insertion date / time |
| Q06Q10 | - |  |  | SI | Nurse / Clinician |
| Q06Q2 | - |  |  | SI | Insertion time |
| Q06Q3 | - |  |  | SI | Day/Shift |
| Q06Q4 | - |  |  | SI | VIP score |
| Q06Q5 | - |  |  | SI | Site visible |
| Q06Q6 | - |  |  | SI | Dressing intact / clean / dated? |
| Q06Q7 | - |  |  | SI | Moisture / Leak from site |
| Q06Q8 | - |  |  | SI | Flow problems / flushed |
| Q06Q9 | - |  |  | SI | Needle-free device / Extension in situ |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| SPEC_CTLOC_DR | bigint |  | FK | SI | Des Ref CTLOC |
| SPEC_Childsub | double |  |  | NO | Childsub |
| SPEC_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| SPEC_CreatedDate | date |  |  | SI | Created Date |
| SPEC_CreatedTime | time |  |  | SI | Created Time |
| SPEC_CreatedUser_DR | bigint |  | FK | SI | Created User |
| SPEC_RowId | varchar |  |  | NO | - |
| SPEC_UpdatedDate | date |  |  | SI | Updated Date |
| SPEC_UpdatedTime | time |  |  | SI | Updated Time |
| SPEC_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*