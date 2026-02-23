# SQLUser.MR_Finding

**Schema:** SQLUser
**Columnas:** 29
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| FIN_ParRef | bigint | PK |  | NO | MR_Adm Parent Reference |
| FIN_Childsub | double |  |  | NO | Childsub |
| FIN_Comment | varchar |  |  | SI | Comment |
| FIN_CreateDate | date |  |  | SI | CreateDate |
| FIN_CreateTime | time |  |  | SI | CreateTime |
| FIN_Date | date |  |  | SI | Date |
| FIN_Deleted | varchar |  |  | SI | Deleted |
| FIN_ICDCode_DR | bigint |  | FK | SI | Des Ref to MRCID |
| FIN_ICPCCode_DR | bigint |  | FK | SI | Des Ref to MRCICPC2 |
| FIN_Laterality | varchar |  |  | SI | Laterality |
| FIN_MasterVersion_DR | varchar |  | FK | SI | Des Ref MRFinding |
| FIN_NoFindingOf | bit |  |  | SI | NoSymptomOf |
| FIN_PhyESystem_DR | varchar |  | FK | SI | Des Ref MRCPhyESystem
only used when finding part... |
| FIN_PhysicalExam_DR | varchar |  | FK | SI | Des Ref MRPhysicalExam
only used when finding par... |
| FIN_RefinedSiteSCTIDs | varchar |  |  | SI | RefinedSiteSCTIDs |
| FIN_RowId | varchar |  |  | NO | - |
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
| Q88Q1 | - |  |  | SI | Time |
| Q88Q2 | - |  |  | SI | mm/Hg |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*