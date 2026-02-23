# SQLUser.PA_PersonAdmInsRef

**Schema:** SQLUser
**Columnas:** 12
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| REF_ParRef | varchar | PK |  | NO | PA_Person Parent Reference |
| REF_CTLOC_DR | bigint |  | FK | SI | Des Ref CTLoc |
| REF_CTPCP_DR | varchar |  | FK | SI | Des Ref CTCareProv |
| REF_Childsub | double |  |  | NO | Childsub |
| REF_DateFrom | date |  |  | SI | DateFrom |
| REF_DateTo | date |  |  | SI | DateTo |
| REF_Dependent_DR | varchar |  | FK | SI | Des Ref PAPersonAdmInsRef |
| REF_EpisSubType_DR | bigint |  | FK | SI | Des Ref EpisSubType |
| REF_Message | varchar |  |  | SI | Message |
| REF_Overide | varchar |  |  | SI | REFOveride |
| REF_RowId | varchar |  |  | NO | - |
| REF_Speciality_DR | bigint |  | FK | SI | Des Ref Speciality |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*