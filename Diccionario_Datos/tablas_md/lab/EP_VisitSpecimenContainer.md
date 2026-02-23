# lab.EP_VisitSpecimenContainer

**Schema:** lab
**Columnas:** 14
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Episodio**. Registros de episodios clínicos.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| VISSC_ParRef | varchar | PK |  | NO | EP_VisitSpecimen Parent Reference |
| VISSC_ContainerNumber | varchar |  |  | SI | VISSC_ContainerNumber |
| VISSC_Container_DR | varchar |  | FK | SI | Container DR |
| VISSC_Medtrak_field1 | varchar |  |  | SI | Medtrak field1 |
| VISSC_Medtrak_field2 | varchar |  |  | SI | Medtrak field2 |
| VISSC_Medtrak_field3 | varchar |  |  | SI | Medtrak field3 |
| VISSC_Medtrak_field4 | varchar |  |  | SI | Medtrak field4 |
| VISSC_Medtrak_field5 | varchar |  |  | SI | VISSC_Medtrak_field5 (Order RowID) |
| VISSC_NotCollected | varchar |  |  | SI | Not Collected yet |
| VISSC_Order | double |  |  | NO | Order Number |
| VISSC_RowID | varchar |  |  | NO | - |
| VISSC_UserSite_DR | varchar |  | FK | SI | User Site DR |
| VISSC_VolumeCollected | double |  |  | SI | Volume Collected |
| VISSC_VolumeCurrently | double |  |  | SI | Volume Currently |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*