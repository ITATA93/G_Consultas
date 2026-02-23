# web_Msg.LBC_CollectionSpecimenContainer

**Schema:** web_Msg
**Columnas:** 22
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Componente Web**. Interfaz de usuario del sistema TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SessionParRef | varchar | PK |  | NO | - |
| ID | varchar |  |  | NO | - |
| LBCCOLSC_AnatomicalSiteMandatory | varchar |  |  | SI | Anatomical Site Mandatory
Flag to indicate if a a... |
| LBCCOLSC_AnatomicalSiteQualifierMandatory | varchar |  |  | SI | Anatomical Site Qualifier Mandatory
Flag to indic... |
| LBCCOLSC_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LBCCOLSC_Container_DR | bigint |  | FK | SI | Container DR |
| LBCCOLSC_DefaultAnatomicalSiteQualifier_DR | varchar |  | FK | SI | Anatomical Site Qualifier |
| LBCCOLSC_DefaultAnatomicalSite_DR | bigint |  | FK | SI | Default anatomical site |
| LBCCOLSC_DefaultLesion_DR | bigint |  | FK | SI | Lesion |
| LBCCOLSC_DefaultVolume | double |  |  | SI | Default Collected Volume |
| LBCCOLSC_LesionMandatory | varchar |  |  | SI | Lesion Mandatory
Flag to indicate if a lesion is ... |
| LBCCOLSC_MinVolume | double |  |  | SI | Min Volume |
| LBCCOLSC_ParRef | bigint |  |  | SI | Parent TestItem DR |
| LBCCOLSC_RowID | varchar |  |  | SI | - |
| LBCCOLSC_SpecimenGroup_DR | bigint |  | FK | SI | Specimen Group |
| LBCCOLSC_SpecimenReusable | varchar |  |  | SI | Specimen Reusable
Specimen Reusability Type to in... |
| LBCCOLSC_Specimen_DR | bigint |  | FK | SI | Specimen DR |
| LBCCOLSC_ValidityTime | integer |  |  | SI | Validity Time
A Specimen received in a Collection... |
| ReadOnly | bit |  |  | SI | - |
| SessionId | varchar |  |  | SI | - |
| childsub | bigint |  |  | NO | - |
| webMsgClassName | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*