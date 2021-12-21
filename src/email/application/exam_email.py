from dataclasses import dataclass
from typing import Any, Dict
from .email_base import EmailBase


@dataclass
class ExamData:
    exam_name: str
    student_padron: str
    student_full_name: str
    corrector_name: str
    correction_details: str
    grade: float
    extra_points: float
    final_grade: float


@dataclass
class ExamEmailData:
    student_email: str
    exam_data: ExamData


class ExamEmail(EmailBase):
    TEMPLATE_PLAIN_DIR = "emails/notas_examen_plain.html"
    TEMPLATE_HTML_DIR = "emails/notas_examen.html"
    WITH_COPY_TO_DOCENTES = True

    def _create_subject(self, data: ExamData) -> str:
        return f"Corrección de {data.exam_name} - Padrón {data.student_padron}"

    def _create_context(self, data: ExamData) -> Dict[str, Any]:
        return {
            "examen": data.exam_name,
            "nombre": data.student_full_name,
            "corrector": data.corrector_name,
            "correcciones": data.correction_details,
            "nota": data.grade,
            "puntos_extras": data.extra_points,
            "nota_final": data.final_grade,
        }

    def send_email(self, data: ExamEmailData) -> None:
        subject = self._create_subject(data.exam_data)
        context = self._create_context(data.exam_data)

        message = self._create_message(data.student_email, subject, context)
        self._message_sender.send(message)

    def preview_email(self, data: ExamEmailData) -> str:
        context = self._create_context(data.exam_data)
        return self._render_html(context)
