# web_Msg.MR_Finding

**Schema:** web_Msg
**Columnas:** 32
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Componente Web**. Interfaz de usuario del sistema TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SessionParRef | varchar | PK |  | NO | - |
| FIN_Childsub | double |  |  | SI | Childsub |
| FIN_CreateDate | date |  |  | SI | CreateDate |
| FIN_CreateTime | time |  |  | SI | CreateTime |
| FIN_Date | date |  |  | SI | Date |
| FIN_Deleted | varchar |  |  | SI | Deleted |
| FIN_Exists | bit |  |  | SI | Finding Exists |
| FIN_ICDCode_DR | bigint |  | FK | SI | Des Ref to MRCID |
| FIN_ICPCCode_DR | bigint |  | FK | SI | Des Ref to MRCICPC2 |
| FIN_Laterality | varchar |  |  | SI | Laterality |
| FIN_MasterVersion_DR | varchar |  | FK | SI | Des Ref MRFinding |
| FIN_NoFindingOf | bit |  |  | SI | NoSymptomOf |
| FIN_ParRef | bigint |  |  | SI | MR_Adm Parent Reference
Required by User.MRFindin... |
| FIN_PhyESystem_DR | varchar |  | FK | SI | Des Ref MRCPhyESystem
only used when finding part... |
| FIN_PhysicalExam_DR | varchar |  | FK | SI | Des Ref MRPhysicalExam
only used when finding par... |
| FIN_RefinedSiteSCTIDs | varchar |  |  | SI | RefinedSiteSCTIDs |
| FIN_RowId | varchar |  |  | SI | - |
| FIN_SeveritySnomed_DR | bigint |  | FK | SI | Des Ref PACSnomedConcept |
| FIN_Severity_DR | bigint |  | FK | SI | Des Ref MRCSeverity |
| FIN_SiteSnomed_DR | bigint |  | FK | SI | Des Ref PACSnomedConcept |
| FIN_SiteText | varchar |  |  | SI | SiteText |
| FIN_SnomedConcept_DR | bigint |  | FK | SI | Des Ref PACSnomedConcept |
| FIN_SnomedTerms_DR | bigint |  | FK | SI | Des Ref PACSnomedTerms |
| FIN_Time | time |  |  | SI | Time |
| FIN_UpdateDate | date |  |  | SI | UpdateDate |
| FIN_UpdateTime | time |  |  | SI | UpdateTime |
| FIN_UpdateUser_DR | bigint |  | FK | SI | Des Ref SSUser |
| ID | varchar |  |  | NO | - |
| ReadOnly | bit |  |  | SI | - |
| SessionId | varchar |  |  | SI | - |
| childsub | bigint |  |  | NO | - |
| webMsgClassName | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*