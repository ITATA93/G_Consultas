# SQLUser.PA_SLADetailsAllocated

**Schema:** SQLUser
**Columnas:** 33
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Detalle de la entidad padre.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SLAD_RowId | bigint | PK |  | NO | - |
| SLAD_APPT_DR | varchar |  | FK | SI | Des Ref APPT |
| SLAD_AdmCoding_DR | varchar |  | FK | SI | Des Ref AdmCoding |
| SLAD_AdmDate | date |  |  | SI | Adm Date |
| SLAD_AdmWardAttend_DR | varchar |  | FK | SI | Des Ref AdmWardAttend |
| SLAD_AdminCat_DR | bigint |  | FK | SI | Des Ref InsType |
| SLAD_Allocated | varchar |  |  | SI | Allocated |
| SLAD_CTCP_DR | varchar |  | FK | SI | Des Ref CTCP |
| SLAD_Comment | varchar |  |  | SI | Comment |
| SLAD_Commissioner_DR | bigint |  | FK | SI | Des Ref HCA |
| SLAD_DateAlloc | date |  |  | SI | Date Allocated |
| SLAD_EffectiveDate | date |  |  | SI | EffectiveDate |
| SLAD_EpisSubtype_DR | bigint |  | FK | SI | Des Ref EpisSubtype |
| SLAD_EpisodeAddress | varchar |  |  | SI | Episode Address |
| SLAD_EpisodeAge | double |  |  | SI | Episode Age |
| SLAD_EpisodeGP | varchar |  |  | SI | Episode GP |
| SLAD_EpisodeType | varchar |  |  | SI | EpisodeType |
| SLAD_GP_DR | bigint |  | FK | SI | Des Ref RefDoc |
| SLAD_HAR_DR | bigint |  | FK | SI | Des Ref HCR |
| SLAD_HRG_DR | bigint |  | FK | SI | Des Ref HRG |
| SLAD_ManualEntry | varchar |  |  | SI | Manual Entry |
| SLAD_PAADM_DR | bigint |  | FK | SI | Des Ref PAADM |
| SLAD_Person_DR | bigint |  | FK | SI | Des Ref Person |
| SLAD_Procedure_DR | bigint |  | FK | SI | Des Ref Procedure |
| SLAD_ReallocateFlag | varchar |  |  | SI | Reallocate Flag |
| SLAD_ServAgreem_DR | bigint |  | FK | SI | Des Ref ServAgreem |
| SLAD_ServiceGroup_DR | bigint |  | FK | SI | Des Ref ServiceGroup |
| SLAD_Specialty_DR | bigint |  | FK | SI | Des Ref CTLOC |
| SLAD_TimeAlloc | time |  |  | SI | Time Alloc |
| SLAD_Trust_DR | bigint |  | FK | SI | Des Ref Trust |
| SLAD_User_DR | bigint |  | FK | SI | Des Ref User |
| SLAD_ValidFlag | varchar |  |  | SI | Valid Flag |
| SLAD_WaitList_DR | bigint |  | FK | SI | Des Ref WaitList |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*