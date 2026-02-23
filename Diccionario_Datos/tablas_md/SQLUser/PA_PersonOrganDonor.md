# SQLUser.PA_PersonOrganDonor

**Schema:** SQLUser
**Columnas:** 5
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ORG_ParRef | bigint | PK |  | NO | PA_Person Parent Reference |
| ORG_Childsub | double |  |  | NO | Childsub |
| ORG_PAPER_DR | bigint |  | FK | SI | Des Ref PAPER |
| ORG_Remarks | varchar |  |  | SI | Remarks |
| ORG_RowId | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*