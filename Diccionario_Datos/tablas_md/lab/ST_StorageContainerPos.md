# lab.ST_StorageContainerPos

**Schema:** lab
**Columnas:** 16
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Stock**. Control de existencias.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| STCP_ParRef | varchar | PK |  | NO | ST_StorageContainer Parent Reference |
| STCP_Accession | varchar |  |  | SI | Accession |
| STCP_Comment | varchar |  |  | SI | Comment |
| STCP_DBVABlockOrder_DR | varchar |  | FK | SI | Accession Block Order DR	  |
| STCP_DateChangeReason | varchar |  |  | SI | Date Change Reason |
| STCP_DisposalDate | date |  |  | SI | Disposal Date |
| STCP_Episode_DR | varchar |  | FK | SI | Episode DR |
| STCP_NextReviewDate | date |  |  | SI | Next Review Date |
| STCP_Position | double |  |  | NO | Position |
| STCP_RequestBy_DR | varchar |  | FK | SI | Requested By DR |
| STCP_ReviewCycle | double |  |  | SI | Review Cycle |
| STCP_RowID | varchar |  |  | NO | - |
| STCP_SpecimenContainer_DR | varchar |  | FK | SI | Specimen Container DR |
| STCP_Specimen_DR | varchar |  | FK | SI | Specimen DR |
| STCP_TemporarilyRemoved | varchar |  |  | SI | Temporarily removed |
| STCP_xxx | varchar |  |  | SI | xxx |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*