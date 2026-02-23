# SQLUser.PA_PersonInsurance

**Schema:** SQLUser
**Columnas:** 18
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| INS_ParRef | bigint | PK |  | NO | PA_Person Parent Reference |
| INS_AuxInsType_DR | bigint |  | FK | SI | Des Ref AuxInsType |
| INS_CTLOC_DR | bigint |  | FK | SI | Des Ref CTSpec |
| INS_CTPCP_DR | varchar |  | FK | SI | Des Ref CTCareProv |
| INS_Childsub | double |  |  | NO | Childsub |
| INS_DateFrom | date |  |  | SI | Date From |
| INS_DateTo | date |  |  | SI | Date To |
| INS_DependentFlag | varchar |  |  | SI | DependentFlag |
| INS_Dependent_DR | varchar |  | FK | SI | Des Ref PAPersonInsurance |
| INS_EpisSubType_DR | bigint |  | FK | SI | Des Ref PACEpisodeSubType |
| INS_HealthFundNo | varchar |  |  | SI | HealthFundNo |
| INS_InsType_DR | bigint |  | FK | SI | Des Ref InsType |
| INS_RowId | varchar |  |  | NO | - |
| INS_Speciality_DR | bigint |  | FK | SI | Des Ref CTSpec |
| INS_UpdateDate | date |  |  | SI | Update Date |
| INS_UpdateHospital_DR | bigint |  | FK | SI | Des Ref UpdateHospital |
| INS_UpdateTime | time |  |  | SI | Update Time |
| INS_UpdateUser_DR | bigint |  | FK | SI | Des Ref UpdateUser |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*