# web_Msg.MR_Diagnos_MRDIA_TumourNotes

**Schema:** web_Msg
**Columnas:** 4
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Diagnósticos**. Códigos CIE-10 asociados al episodio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| MR_Diagnos | varchar | PK |  | NO | Parent reference |
| ID | varchar |  |  | NO | - |
| MRDIA_TumourNotes | varchar |  |  | SI | MRDIA_TumourNotes |
| element_key | varchar |  |  | NO | MRDIATumourNotes array key |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*